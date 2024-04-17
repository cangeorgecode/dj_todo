from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

def index(request):
    todo = Todo.objects.all()
    completed = Todo.objects.filter(isDone=True).count()
    total = Todo.objects.count()
    progress = completed/total*100
    context = {
        'todo': todo,
        'total': total,
        'completed': completed,
        'progress': progress,
    }
    return render(request, 'todo/index.html', context)

def addtodo(request):
    form = TodoForm()
    context = {
        'form': form,
    }
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'todo/addtodo.html', context)
    return render(request, 'todo/addtodo.html', context)

def readtodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    context = {
        'todo': todo,
    }
    return render(request, 'todo/readtodo.html', context)

def updatetodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    form = TodoForm(instance=todo)
    context = {
        'todo': todo,
        'form': form,
    }
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'todo/updatetodo.html', context)

def deletetodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.delete()
    return redirect('index')