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

@login_required(login_url="/settings/")
def settings(request):
    if request.method == "POST":
        manager_id = request.POST.get('manager_id')
        if request.POST.get('delete_manager_'+manager_id) == "delete":
            manager = Manager.objects.get(id=manager_id)
            manager.delete()
            return redirect('/managers/')
        else:
            return redirect('/edit_manager/'+request.POST.get('manager_id'))
    else:
        settings = Settings.objects.all()
        return render(request,'settings.html',{'settings': settings })

