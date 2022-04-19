from django import forms
from .models import *

class registerform(forms.Form):
    name    = forms.CharField(max_length=20)
    email    = forms.CharField(max_length=20)
    number    = forms.IntegerField()
    subject    = forms.CharField(max_length=20)
    message    = forms.CharField(max_length=200)