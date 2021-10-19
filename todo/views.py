from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Vazifa
from .forms import TaskForm
# Create your views here.

@login_required 
def index(request):
    user = request.user
    
    tasks=Vazifa.objects.all().order_by('-pk').filter(user=request.user)

    form=TaskForm()

    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
        return redirect('todo')

    context={'tasks':tasks,'form':form}
    return render(request,'todoapp/list.html',context)

@login_required 
def updateTask(request,pk):
    task=Vazifa.objects.get(id=pk)

    form=TaskForm(instance=task)

    if request.method=='POST':
        form=TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo')

    context={'form':form}

    return render(request,'todoapp/update_task.html',context)

@login_required 
def  deleteTask(request,pk):
    item=Vazifa.objects.get(id=pk)

    if request.method=='POST':
        item.delete()
        return redirect('todo')

    context={'item':item}
    return render(request, 'todoapp/delete.html',context)

