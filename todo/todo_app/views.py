from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import *
from .forms import *


def index(request):
    query = request.GET.get('q')

    if query:
        tasks = task.objects.filter(Q(title__icontains=query) | Q(text__icontains=query))
    else:
        tasks = task.objects.all()

    context = {
        'title': 'Список задач',
        'tasks': tasks
    }
    return render(request, 'todo_app/index.html', context)


def task_detail(request, task_id):
    task_key = task.objects.get(id=task_id)
    data_key = file.objects.filter(task_id=task_id)
    context = {
        'title': f'Задача [{task_key.title}]',
        'data': data_key,
        'task': task_key,
        'number': (task_key.out_date - task_key.in_date).days,
    }
    return render(request, 'todo_app/task.html', context)


def task_add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm()

    context = {
        'title': 'Добавление записи',
        'form': form
    }
    return render(request, 'todo_app/add.html', context)


def task_edit(request, task_id):
    task_key = task.objects.get(id=task_id)
    data_key = file.objects.filter(task_id=task_id)
    upload = file()
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task_key)
        if request.FILES.get('file_data', False):
            upload.task_id = task.objects.get(id=task_id)
            upload.path = request.FILES['file_data']
            upload.save()
            return redirect('task_edit', task_id)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm()
    context = {
        'title': f'Редактирование записи [{task_key.title}]',
        'form': form,
        'task': task_key,
        'data': data_key,
        'number': (task_key.out_date - task_key.in_date).days,
    }
    return render(request, 'todo_app/edit.html', context)


def task_delete(request, task_id):
    task_key = task.objects.get(id=task_id)
    task_key.delete()
    return redirect('index')


def file_delete(request, file_id):
    file_key = file.objects.get(id=file_id)
    file_key.delete()
    return redirect('task_edit', file_key.task_id.id)
