from __future__ import unicode_literals

from django.db import models

from django_celery_beat.models import CrontabSchedule, PeriodicTask


# Create your models here.
class Schedule(models.Model):
    id              = models.AutoField(primary_key=True)
    celery_sched_id = models.IntegerField(null=True)
    celery_task_id  = models.IntegerField(null=True)
    name            = models.CharField(max_length=256)
    minute          = models.CharField(max_length=2)
    hour            = models.CharField(max_length=2)
    week            = models.CharField(max_length=2)
    month           = models.CharField(max_length=2)
    year            = models.CharField(max_length=2)
    enabled         = models.BooleanField(default=True)

class BackupSchedule(models.Model):
    id          = models.AutoField(primary_key=True)
    vm          = models.ForeignKey('manager.VM')
    schedule    = models.ForeignKey('Schedule')
    