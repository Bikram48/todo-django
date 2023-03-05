from django.shortcuts import render
from .forms import TaskForm

# Create your views here.
def create_task(request):

    form = TaskForm()

    context = {
        "form": form
    }

    return render(request, "task_form.html", context=context)