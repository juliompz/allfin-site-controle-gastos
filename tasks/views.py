
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .form import TaskForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def taskList(request):
    data = {}
    data['tasks']= Task.objects.all().order_by('-created_date').filter(user=request.user)
    return render(request, 'tasks/tasks.html', data)

@login_required
def taskView(request, id):
    data = {}
    data['task'] = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', data)

@login_required
def taskAdd(request):
    data = {}
    taskForm = TaskForm(request.POST or None)
    if taskForm.is_valid():
        task = taskForm.save(commit= False)
        task.done = 'doing'
        task.user = request.user 
        task.save()
        return redirect('list')
    data['taskForm'] = taskForm
    return render(request, 'tasks/newTask.html', data)

@login_required
def updateTask(request, id):
    data = {}
    task = Task.objects.get(pk = id)
    taskForm = TaskForm(request.POST or None, instance= task)
    if taskForm.is_valid():
        taskForm.save()
        return redirect('list')
    data['taskForm'] = taskForm
    data['task'] = task
    return render(request, 'tasks/newtask.html', data)

@login_required
def deleteTask(request, id):
    data = {}
    task = Task.objects.get(pk = id)
    task.delete()
    messages.info(request, 'Tarefa deletada com sucesso!')
    return redirect('list')

@login_required
def yourname(request, nome):
    data = {}
    data['nome'] = nome
    return render(request, 'tasks/yourname.html', data)

