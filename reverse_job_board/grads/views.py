from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.dispatch import receiver
from django.views import View

from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Graduate

import requests
from bs4 import BeautifulSoup
# Create your views here.


def index(request):
    # order graduates by first name and list everyone on the index

    order_grads = Graduate.objects.order_by('first_name')
    return render(request, 'grads/index.html', {'order_grads':order_grads})


def grad_detail(request, pk):
    """
    Take the graduate's github url and parse some information off
    the pinned repositories section on the profile page.

    Todo:
        Test for pinned repos
        Remove unused content

    """
    grad = get_object_or_404(Graduate, pk=pk)
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

    profileurl = Graduate.objects.get(first_name=id)

    return render(request, 'grads/profile.html', {'profileurl':profileurl})

class CreateProfileView(LoginRequiredMixin, View):

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_grad_detail(sender, created, instance, **kwargs):
        pass
