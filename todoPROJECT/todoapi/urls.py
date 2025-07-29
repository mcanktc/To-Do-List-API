from django.urls import path
from . import views

urlpatterns = [
    path('tasks', views.TodoSystem.as_view(), name='todos')

]