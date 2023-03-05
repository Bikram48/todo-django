from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import *

# Create your views here.
def create_task(request):

    form = TaskForm()
    task = Task()

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