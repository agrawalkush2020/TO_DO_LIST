from django.shortcuts import render, redirect
from .forms import TaskCreateForm
from .models import Task

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            task_added_form = TaskCreateForm(request.POST)
            if task_added_form.is_valid():
                task=task_added_form.save(commit=False)
                task.user=request.user 
                task_added_form.save()

        tasks = Task.objects.filter(user=request.user)
        task_form = TaskCreateForm()
        return render(request, 'tasks/index.html', {"tasks": tasks, "taskform": task_form})
    else:
        return redirect('invalid', message='User needs to login first to see the tasks')

