from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='grads'),
    url(r'^grad/(?P<slug>[\w-]+)/$', views.grad_detail, name='grad_detail'),
    url(r'^profile/(?P<slug>[\w-]+)/$', views.get_profleurl),
    url(r'^edit/$', views.EditProfileView.as_view(), name='grad_profile'),
]
