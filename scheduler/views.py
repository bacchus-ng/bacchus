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
# Create your views here.


@login_required(login_url="/login/")
def list_sched(request):
    scheds = Schedules.objects.all()
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
        sched = Schedules(name=sched_name,minute=sched_min,hour=sched_hour,week=sched_week,month=sched_month,year=sched_year)
        sched.save()
        celery_sched = CrontabSchedule.objects.create(minute=sched_min,hour=sched_hour,day_of_week=sched_week,day_of_month=sched_month,month_of_year=sched_year)
        PeriodicTask.objects.create(crontab=celery_sched,name=sched_name,task='scheduler.tasks.run_schedule',args=sched.id)
        
        # refresh celery_beat here to reflect the changes
        
        vmlist = request.POST.getlist('schedvmlist')
        for vmid in vmlist:
            vm = VM.objects.get(vmid=vmid)
            vm.schedule = sched
            vm.protected = True
            vm.save()
        
        scheds = Schedules.objects.all()
        return render(request,'schedules.html',{'scheds': scheds })
    else:
        vms = VM.objects.all()
        return render(request,'definesched.html',{'vms': vms })

