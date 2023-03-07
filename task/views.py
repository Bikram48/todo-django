from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import TaskForm
from .models import *

# Create your views here.
def register_user(request):

    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

    context = {
        "form": form
    }

    return render(request, "register.html", context)

def create_task(request):

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        "form": form
    }

    return render(request, "task_form.html", context=context)

def view_tasks(request):

    task = Task.objects.all()

    context = {
        "tasks": task
    }

    return render(request, "all_tasks.html", context)

def update_task(request, id):

    task = Task.objects.get(id=id)

    form = TaskForm(instance=task)
    if(request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('/tasks')

    context = {
       "form": form
    }
    return render(request, "task_form.html", context=context)

def remove_task(request, id):
    
    task = Task.objects.get(id=id)

    context = {
        "task": task
    }

    if request.method=="POST":
        task.delete()
        return redirect('/tasks')

    return render(request, "task_delete.html", context=context)