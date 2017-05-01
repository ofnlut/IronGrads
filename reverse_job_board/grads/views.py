from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Graduate
# Create your views here.

#order graduates by first name and list everyone on the index
def index(request):
    order_grads = Graduate.objects.order_by('first_name')
    return render(request, 'grads/index.html', {'order_grads':order_grads})

def info(request):
    return HttpResponse("info here!")
