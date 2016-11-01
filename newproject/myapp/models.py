from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Result(models.Model):
    user_name = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    email = models.CharField(max_length = 20)
