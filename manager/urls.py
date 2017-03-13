from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^managers/$', views.managers, name='managers'),
    url(r'^add_manager/$', views.add_manager, name='add_manager'),
]
