from django import forms

from .models import Manager

class ManagerForm(forms.ModelForm):
    
    class Meta:
        model = Manager
        fields = ('name','fqdn','url','username','password',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'mymanager', 'onfocus':'this.placeholder = \'\''}),
            'fqdn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'mymanager.local.domain', 'onfocus':'this.placeholder = \'\''}),
            'url': forms.TextInput(attrs={'class': 'form-control','placeholder': 'https://mymanager.local.domain/ovirt-engine/api', 'onfocus':'this.placeholder = \'\'' }),
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'admin@internal', 'onfocus':'this.placeholder = \'\''}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }