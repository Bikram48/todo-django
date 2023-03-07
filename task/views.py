from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TaskForm, CreateUserForm
from .models import *

# Create your views here.
def register_user(request):

    if request.user.is_authenticated:
        return redirect('add_task')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)

            if form.is_valid():
                form.save()

        context = {
            "form": form
        }

    return render(request, "register.html", context)

def signin_user(request):
    if request.user.is_authenticated:
        return redirect('add_task')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('add_task')
            else:
                messages.info(request, "username or password doesn't exist")

    return render(request, "login.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, "You successfully logged out")
    return redirect('login')

@login_required(login_url='login')
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

@login_required(login_url='login')
def view_tasks(request):

    task = Task.objects.all()

    context = {
        "tasks": task
    }

    return render(request, "all_tasks.html", context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def remove_task(request, id):
    
    task = Task.objects.get(id=id)

    context = {
        "task": task
    }

    if request.method=="POST":
        task.delete()
        return redirect('/tasks')

    return render(request, "task_delete.html", context=context)