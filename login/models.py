from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Dashboard(models.Model):
    manager_count   =  models.IntegerField(default=0)
    host_count      =  models.IntegerField(default=0)
    vm_count        =  models.IntegerField(default=0)
    total_backup    =  models.FloatField()
    total_capacity  =  models.FloatField()
    success_rate    =  models.IntegerField(default=100)
