from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from models import *
from manager.models import *
from django_celery_beat.models import CrontabSchedule, PeriodicTask
import json
import os
from celerytools import CeleryTools

# Create your views here.

@login_required(login_url="/login/")
def list_sched(request):
    if request.method == "POST":
        if request.POST.get('delete_sched') == "delete":

            sched_id = request.POST.get('sched_id')
            sched = Schedule.objects.get(id=sched_id)
            # delete celery schedule entries
            celery_task = PeriodicTask.objects.get(id=sched.celery_task_id)
            celery_task.delete()
            
            celery_sched = CrontabSchedule.objects.get(id=sched.celery_sched_id)
            celery_sched.delete()
            
            # delete db schedule entries
            backupscheds = BackupSchedule.objects.all().filter(schedule=sched)
            for backupsched in backupscheds:
                backupsched.delete()
            
            sched.delete()
            CeleryTools.restart_beat()
        else:
            return redirect('/editsched/'+request.POST.get('sched_id'))
        
    scheds = Schedule.objects.all()
    
    return render(request,'schedules.html',{'scheds': scheds })

@login_required(login_url="/login/")
def define_sched(request):
    if request.method == "POST":
        
        sched_name = request.POST.get('sched_name')
        sched_min = request.POST.get('sched_min')
        sched_hour = request.POST.get('sched_hour')
        sched_week = request.POST.get('sched_week')
        sched_month = request.POST.get('sched_month')
        sched_year = request.POST.get('sched_year')
        sched = Schedule(name=sched_name,minute=sched_min,hour=sched_hour,week=sched_week,month=sched_month,year=sched_year)
        sched.save()
        celery_sched = CrontabSchedule.objects.create(minute=sched_min,hour=sched_hour,day_of_week=sched_week,day_of_month=sched_month,month_of_year=sched_year)
        sched_args = json.dumps([sched.id])
        sched.celery_sched_id = celery_sched.id
        sched.save()
        
        celery_task = PeriodicTask.objects.create(crontab=celery_sched,name=sched_name,task='scheduler.tasks.run_schedule',args=sched_args)
        sched.celery_task_id = celery_task.id
        sched.save()
        
        # refresh celery_beat here to reflect the changes
        CeleryTools.restart_beat()
        
        vmlist = request.POST.getlist('schedvmlist')
        for vmid in vmlist:
            vm = VM.objects.get(vmid=vmid)
            backupsched = BackupSchedule(vm=vm,schedule=sched)
            backupsched.save()      
        
        return redirect('/schedules/')

    else:
        vms = VM.objects.all()
        return render(request,'definesched.html',{'vms': vms })


@login_required(login_url="/login/")
def list_maint(request):
    list_maint = 0  
    return render(request,'listmaint.html',{'list_maint': list_maint })

@login_required(login_url="/login/")
def delete_sched(request):
    if request.method == "POST":
        sched_id = request.POST.get('sched_id')
        
    scheds = Schedule.objects.all()
    return render(request,'schedules.html',{'scheds': scheds })


@login_required(login_url="/login/")
def edit_sched(request, sched_id):
       
    sched = Schedule.objects.get(id=sched_id)
    minutes = range(0,60)
    minutes.insert(0,'*')
    hours = range(0,24)
    hours.insert(0,'*')
    days = range(1,32)
    days.insert(0,'*')
    months = range(1,13)
    months.insert(0,'*')
    
    return render(request,'editsched.html',{'sched': sched,'minutes': minutes, 'hours': hours, 'days':days, 'months':months })




