from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from manager.vmtools import *
from models import *
# Create your views here.

@login_required(login_url="login/")
def home(request):
	
	dash = Dashboard(manager_count=VMTools.manager_count(),host_count=VMTools.host_count(),vm_count=VMTools.vm_count(),total_backup=VMTools.total_backup_size(),success_rate=VMTools.backup_success_rate())
	
	return render(request,"dashboard.html",{'dash': dash })

