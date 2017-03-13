from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from models import *
import ovirtsdk4 as sdk
import ovirtsdk4.types as types

def list_managers():
        return Manager.objects.all()

def managers(request):
        managers = list_managers()
        return render(request,'managers.html',{'managers': managers })

def add_manager(request):
        managers = list_managers()
        return render(request,)

