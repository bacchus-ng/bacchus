from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^schedules/$', views.list_sched, name='scheds'),
    url(r'^definesched/', views.define_sched, name="definesched"),    
]
