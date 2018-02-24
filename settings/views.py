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
        for key in request.POST:
            print(key)
            value = request.POST[key]
            print(value)
            
    settings = Settings.objects.all()
    return render(request,'settings.html',{'settings': settings })

