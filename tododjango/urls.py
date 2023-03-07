"""tododjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', create_task, name='add_task'),
    path('tasks/', view_tasks, name="tasks"),
    path('update/<int:id>', update_task, name="update_task"),
    path('delete/<int:id>', remove_task, name="delete_task"),
    path('register/', register_user, name='register'),
    path('login/', signin_user, name='login')
]
