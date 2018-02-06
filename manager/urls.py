from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^managers/$', views.managers, name='managers'),
    url(r'^add_manager/$', views.add_manager, name='add_manager'),
    url(r'^edit_manager/(?P<manager_id>\d+)/$', views.edit_manager, name='edit_manager'),
    url(r'^vms/$', views.list_vms, name='vms'),
    url(r'^runbackup/$', views.run_backup, name='vms'),
    url(r'^tasks/$', views.list_tasks, name='tasks'),
    
    
]

