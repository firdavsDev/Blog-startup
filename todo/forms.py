from django import forms
from django.forms import ModelForm

from .models import Vazifa

class TaskForm(forms.ModelForm):
    class Meta:
        model=Vazifa
        fields=['mavzu','tugadi',]