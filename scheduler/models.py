from __future__ import unicode_literals

from django.db import models



# Create your models here.
class Schedule(models.Model):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=256)
    minute      = models.CharField(max_length=2)
    hour        = models.CharField(max_length=2)
    week        = models.CharField(max_length=2)
    month       = models.CharField(max_length=2)
    year        = models.CharField(max_length=2)
    enabled     = models.BooleanField(default=True)

class BackupSchedule(models.Model):
    id          = models.AutoField(primary_key=True)
    vm          = models.ForeignKey('manager.VM')
    schedule    = models.ForeignKey('Schedule')
    