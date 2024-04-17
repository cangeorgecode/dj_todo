from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.addtodo, name='addtodo'),
    path('read/<todo_id>', views.readtodo, name='readtodo'),
    path('update/<todo_id>', views.updatetodo, name='updatetodo'),
    path('delete/<todo_id>', views.deletetodo, name='deletetodo'),
]