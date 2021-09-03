from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required #oldin login bajariladi sung boshqa url/ utadi sittings.py ----> LOGIN_URL = 'login'  qushish kerak 
#from django.contrib.auth.forms import UserCreationForm #registratsiyadan utish uchun tayor
from django.contrib import messages #xabarlar
#forms.py
from .forms import UserregisterForm, UserUpdateForm,ProfileUpdateForm
# Create your views here.

#ruyhatdan o'tish
def rigester(request):
    if request.method == 'POST':

        form = UserregisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'{username} Akounti yaratildi! Login bo\'lib kirishingiz mumkin!!!')
            return redirect('login')
    else:
        form = UserregisterForm()
    return render(request, 'users/rigester.html',{'form':form})


@login_required #profilga utish uchun oldin login qismdan utish kerak buladi
def profile(request):

    if request.method =='POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile) #faylarni ushlab qolishi uchun
        if u_form.is_valid() and p_form.is_valid():
            username = u_form.cleaned_data.get('username')
            u_form.save()
            p_form.save()
            messages.success(request, f'{username} Profile yangilandi!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form': p_form
    }

    return render (request,'users/profile.html',context)