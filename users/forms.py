from django.forms import fields

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#models
from .models import Profile

#ruyhatdan utish
class UserregisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

#User Update form
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

#Profile update
class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image'] 
