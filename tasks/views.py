from django.shortcuts import render, redirect
from .forms import TaskCreateForm
from .models import Task

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            task_added_form = TaskCreateForm(request.POST)
            if task_added_form.is_valid():
                task = TaskCreateForm(value=task_added_form.cleaned_data['event'], user=request.user)
                task.save()

        tasks = Task.objects.filter(user=request.user)
        task_form = TaskCreateForm()
        return render(request, 'tasks/index.html', {"tasks": tasks, "taskform": task_form})
    else:
        return redirect('invalid', message='User needs to login first to see the tasks')

