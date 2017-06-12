from __future__ import unicode_literals

from django.db import models
from django.db.models import signals
from django.conf import settings
from PIL import Image

# Create your models here.

class Graduate(models.Model):
    author = models.ForeignKey('auth.User')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='details', null=True)
    first_name = models.CharField(max_length=300, default="Iron")
    last_name = models.CharField(max_length=300, default="Yard")
    job_title = models.CharField(max_length=300, default="Web Developer")
    Email = models.CharField(max_length=1000)
    Github = models.URLField(max_length=600, blank=True)
    Linkedin = models.URLField(max_length=600, blank=True)
    Picture = models.ImageField(upload_to='portait/', blank=True)


    class Meta:
         order_with_respect_to = 'first_name'

    def __str__(self):
        return self.first_name
