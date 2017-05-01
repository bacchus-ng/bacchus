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
    if request.method == "POST":
        manager_id = request.POST.get('manager_id')
        if request.POST.get('delete_manager_'+manager_id) == "delete":
            manager = Manager.objects.get(id=manager_id)
            manager.delete()
            return redirect('/managers/')
        else:
            return redirect('/edit_manager/'+request.POST.get('manager_id'))
    else:
        managers = Manager.objects.all()
        return render(request,'managers.html',{'managers': managers })

@login_required(login_url="/login/")
def add_manager(request):
        if request.method == "POST":
            manager = Manager()
            manager.name = request.POST.get('manager_name')
            manager.fqdn = request.POST.get('manager_fqdn')
            manager.url = request.POST.get('manager_url')
            manager.username = request.POST.get('manager_username')
            manager.password = request.POST.get('manager_password')            
            if request.POST.get('manager_save'):
                manager.version = "4.0"
                manager.discovered = VMTools.local_now()
                manager.updated = VMTools.local_now()
                manager.save()
                VMTools.run_dc_inv()
                VMTools.run_cluster_inv()
                VMTools.run_vm_inv()
                return redirect('/managers/')
            elif request.POST.get('manager_verify'):
                               
                if VMTools.verify_manager_connection(manager):
                    verified = True
                else:
                    verified = False
                
                return render(request, 'add_manager.html', {'manager': manager , 'verified':verified })
            else:
                return redirect('/managers/')
                
        else:
            return render(request, 'add_manager.html') 
    
@login_required(login_url="/login/")
def edit_manager(request,manager_id):
        if request.method == "GET":
            manager = Manager.objects.get(id=manager_id)
            return render(request, 'edit_manager.html', {'manager': manager})

        else:
            manager = Manager.objects.get(id=request.POST.get('manager_id'))
            manager.name = request.POST.get('manager_name')
            manager.fqdn = request.POST.get('manager_fqdn')
            manager.url = request.POST.get('manager_url')
            manager.username = request.POST.get('manager_username')
            manager.password = request.POST.get('manager_password')            
                
            if request.POST.get('manager_save'):                
                manager.save()
                return redirect('/managers/')
            elif request.POST.get('manager_verify'):
                               
                if VMTools.verify_manager_connection(manager):
                    verified = True
                else:
                    verified = False
                
                return render(request, 'edit_manager.html', {'manager': manager , 'verified':verified })
            else:
                return redirect('/managers/')
                
             

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




