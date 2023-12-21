from django import forms
from django .contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username= forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your Username',
        'class':'form-control form-control-lg'
    }))
    password= forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your Password',
        'class':'form-control form-control-lg',
        'type':'password'
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2')
    username= forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your Username',
        'class':'form-control form-control-lg'
    }))
    email= forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your Email',
        'class':'form-control form-control-lg'
    }))
    password1= forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your Password',
        'class':'form-control form-control-lg',
        'type':'password'
    }))
    password2= forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Confirm password',
        'class':'form-control form-control-lg',
        'type':'password'

    }))