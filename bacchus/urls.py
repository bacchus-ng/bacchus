"""bacchus URL Configuration

"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login, {'template_name': 'login.html' },name="login"),
    url(r'^logout/', views.logout, {'next_page': '/login'}),
    url(r'', include('login.urls')),
    url(r'', include('manager.urls')),
    url(r'', include('scheduler.urls')),
    url(r'', include('settings.urls')),
    
]
