from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^schedules/$', views.list_sched, name='scheds'),
    url(r'^definesched/$', views.define_sched, name="definesched"),
    url(r'^editsched/(?P<sched_id>\d+)/$', views.edit_sched, name="editsched"),
    url(r'^maintenance/$', views.list_maint, name="list_maint"),    
]
