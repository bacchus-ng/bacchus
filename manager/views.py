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
import ovirtsdk4 as sdk
import ovirtsdk4.types as types
from vmtools import *
from tasks import *

from .forms import ManagerForm


def list_managers():
        return Manager.objects.all()

@login_required(login_url="/login/")
def managers(request):
        managers = Manager.objects.all()
        return render(request,'managers.html',{'managers': managers })

@login_required(login_url="/login/")
def add_manager(request):
        if request.method == "POST":
            form = ManagerForm(request.POST)
            if (form.is_valid()):
                manager = form.save(commit=False)                
                manager.version = "4.0"
                manager.discovered = VMTools.local_now()
                manager.updated = VMTools.local_now()
                manager.save()
                VMTools.run_dc_inv()
                VMTools.run_cluster_inv()
                VMTools.run_vm_inv()
                return redirect('/managers/',)
            
        else:
            manager = ManagerForm()
            
        return render(request, 'add_manager.html', {'manager': manager}) 

@login_required(login_url="/login/")
def list_vms(request):
    vms = VM.objects.all()
    return render(request,'vms.html',{'vms': vms })

@login_required(login_url="/login/")
def run_backup(request):
    if request.method == "POST":
        vmlist = request.POST.getlist('backupvmlist')
        for vmname in vmlist:
            vm = VM.objects.get(name=vmname)
            job = backup_vm.delay(vm.cluster.dc.manager.name,vm.name)
            
        return render(request,'backup.html',{'vms': vmlist })
    else:
        vms = VM.objects.all()
        return render(request,'runbackup.html',{'vms': vms })


@login_required(login_url="/login/")
def list_tasks(request):
    tasks = VmBackups.objects.all().order_by('start').reverse()
    
    if request.is_ajax():
        
        return render(request,'tasks_history_table.html',{'tasks': tasks })
    
    return render(request,'tasks.html',{'tasks': tasks })




