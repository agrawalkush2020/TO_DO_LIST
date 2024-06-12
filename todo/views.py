from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .models import Task,User
from .forms import SignUpForm, loginform, taskform
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def index(request,email=None):

    if email is None:
        return redirect ('invlalid', message='User need to Login-First to see the Tasks')
    
    user=User.objects.get(email=email)
    tasks = user.tasks.all()
    task_form=taskform()
    return render(request, 'todo/index.html',{"tasks":tasks, "taskform":task_form})

def invalid(request,message):
    return render(request, 'todo/invalid.html',{"message":message})

def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        if user_form.is_valid():
            if user_form.cleaned_data['password']!=user_form.cleaned_data['confirm_password']:
                return redirect ('invlalid', message='password does not match with confirm_password')
            user=User(
                        name=user_form.cleaned_data['name'], 
                        email=user_form.cleaned_data['email'],
                        password=user_form.cleaned_data['password']
                    )
            user.save()
            return redirect('login')
    else:
        user_form = SignUpForm()
        return render(request, 'todo/signup.html',{'user_form': user_form})

def login(request):
    if request.method == 'POST':
        user_login_form = loginform(request.POST)
        if user_login_form.is_valid():
            email = user_login_form.cleaned_data['email']
            password = user_login_form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
                if password==user.password:
                    return redirect('index', email=user.email)
                else:
                    return redirect('invalid', message='Incorrect password')
            except User.DoesNotExist:
                return redirect('invalid', message='There is NO user with this Email')

    user_login_form = loginform()
    return render(request, 'todo/login.html',{'user_form':user_login_form})







