# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-13 20:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grads', '0003_graduate_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduate',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
