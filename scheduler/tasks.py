from __future__ import absolute_import 
from celery import shared_task
from django.utils import timezone
from datetime import datetime
from manager.vmtools import *
from scheduler.models import *
from manager.tasks import *

@shared_task
def run_schedule(sched_id):
    sched = Schedule.objects.get(id=sched_id)
    backupscheds = BackupSchedule.objects.filter(schedule=sched)
    for backupsched in backupscheds:
        backup_vm.delay(backupsched.vm.cluster.dc.manager.name,backupsched.vm.name)        
    return True

