from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.

class Settings(models.Model):
    parameter       = models.CharField(max_length=256,null=True)
    value           = models.CharField(max_length=256,null=True)
    updated         = models.DateTimeField(auto_now=True)
