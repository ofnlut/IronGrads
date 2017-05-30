from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^grad/(?P<pk>\d+)/$', views.grad_detail, name='grad_detail')
]
