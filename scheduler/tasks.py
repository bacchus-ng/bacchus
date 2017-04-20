from __future__ import absolute_import 
from celery import shared_task
from django.utils import timezone
from datetime import datetime
from celery.utils.log import get_task_logger
from celery.decorators import periodic_task
from celery import Celery
from celery.schedules import crontab
from manager.vmtools import *

app = Celery()

@shared_task
def run_schedule(sched):
    vms = VM.objects.filter(schedule=sched).get()
    for vm in vms:
        backup_vm.delay(vm.cluster.dc.manager.name,vm.name)
        
    return True