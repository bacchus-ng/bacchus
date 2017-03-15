from django import forms

from .models import Manager

class ManagerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Manager
        fields = ('name','fqdn','url','username','password',)