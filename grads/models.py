from __future__ import unicode_literals

from django.db import models
from django.db.models import signals
from django.conf import settings
from PIL import Image
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.

class Graduate(models.Model):
    author = models.ForeignKey('auth.User', null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='details', null=True)
    slug = models.SlugField(unique=True, blank=True)
    first_name = models.CharField(max_length=300, default="Iron")
    last_name = models.CharField(max_length=300, default="Yard")
    job_title = models.CharField(max_length=300, default="Web Developer")
    Email = models.CharField(max_length=1000)
    Github = models.URLField(max_length=600, blank=True)
    Linkedin = models.URLField(max_length=600, blank=True)
    Picture = models.ImageField(upload_to='portait/', blank=True)


    def save(self, *args, **kwargs):
        if not self.id:
            self.last_pk = User.objects.latest('pk')
            self.first_name = self.last_pk.first_name
            self.slug = slugify(self.first_name).title()
        super(Graduate, self).save(*args, **kwargs)

    class Meta:
         ordering = ['first_name']

    def __str__(self):
        return self.first_name
