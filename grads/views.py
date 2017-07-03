from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.dispatch import receiver
from django.views.generic.edit import UpdateView
from django.views import View

from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy

from .models import Graduate
from .forms import EditProfileForm

import requests
from bs4 import BeautifulSoup
# Create your views here.


def index(request):
    # order graduates by first name and list everyone on the index

    order_grads = Graduate.objects.order_by('first_name')
    return render(request, 'grads/index.html', {'order_grads':order_grads})


def grad_detail(request, slug):
    """
    Take the graduate's github url and parse some information off
    the pinned repositories section on the profile page.

    Todo:
        Test for pinned repos
        Remove unused content

    """
    grad = get_object_or_404(Graduate, slug=slug)
    grad_url = Graduate.objects.get(first_name=grad).Github[17:]

    grad_repos = requests.get(Graduate.objects.get(first_name=grad).Github)
    soup = BeautifulSoup(grad_repos.text, 'html.parser')


    repos = soup.find_all("div", {'class' : 'pinned-repo-item-content', })

    parsed_repo = []
    for repo in repos:
        pinned_repo = {
            'title': repo.find('span', {'class': 'repo js-repo'}).get_text(),
            'disc': repo.find('p', {'class': 'pinned-repo-desc'}).get_text(),
            'link': repo.find('a', href=True)['href']
        }

        parsed_repo.append(pinned_repo)

    #take the parse context to be used in our template.
    context = {
        'grad':grad,
        'grad_url':grad_url,
        'grad_repos':grad_repos,
        'parsed_repo':parsed_repo,
        'repos':repos,
    }

    return render(request, 'grads/grad_detail.html', context)

def get_profleurl(request, id):

    # Generate a url based off the users

    profileurl = Graduate.objects.get(first_name=id)

    return render(request, 'grads/profile.html', {'profileurl':profileurl})

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_grad_detail(sender, created, instance, **kwargs):
    if created:
        Graduate.objects.create(user=instance)

class EditProfileView(LoginRequiredMixin, UpdateView):
    """
    Allows logged in graduates to edit their profile.

    Todo:
        Write tests
    """
    template_name = 'grads/edit_profile.html'
    success_url = reverse_lazy('grads')
    model = Graduate
    fields = ('first_name','last_name','job_title','Email','Linkedin')

    def get_context_data(self, **kwargs):
        context = super(EditProfileView, self).get_context_data(**kwargs)
        context['User'] = User.objects.order_by('username')
        return context

    def get_object(self):
        username = self.request.user
        grad_user = Graduate.objects.get(user=username)

        if self.request.method == 'POST':
            form = EditProfileForm(data=self.request.POST, instance=grad_user)
            if form.is_valid():
                form.save()
        return get_object_or_404(Graduate, user=username)
