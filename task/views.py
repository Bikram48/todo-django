from django.shortcuts import render

# Create your views here.
def create_task(request):
    return render(request, "task_form.html", {})