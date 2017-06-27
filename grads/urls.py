from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='grads'),
    url(r'^grad/(?P<pk>\d+)/$', views.grad_detail, name='grad_detail'),
    url(r'^profile/(?P<id>.+?)/$', views.get_profleurl),
    url(r'^edit/$', views.EditProfileView.as_view(), name='grad_profile'),
]
