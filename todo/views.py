from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .models import Task,User
from .forms import SignUpForm, loginform
from django.contrib.auth.hashers import make_password

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    return render(request, 'todo/index.html',{"tasks":tasks})

def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        if user_form.is_valid():
            if user_form.cleaned_data.password!=user_form.cleaned_data.confirm_password:
                return render(request,'todo/invlalid.html', {'message': 'password does not match with confirm_password'})
            user=User(name=user_form.cleaned_data.name, email=user_form.cleaned_data.username,password=make_password(user_form.cleaned_data.password))
            user.save()
            return render(request, 'todo/signin.html')
    user_form = SignUpForm()
    return render(request, 'todo/signup.html',{'user_form': user_form})

def login(request):
    if request.method == 'POST':
        user_login_form = loginform(request.POST)
        if user_login_form.is_valid():
            user = User.objects.get(email = user_login_form.cleaned_data.email,password=make_password(user_login_form.cleaned_data.password))
            if user is not None:
                redirect('index')

    user_login_form = loginform()
    return render(request, 'todo/login.html',{'user_form':user_login_form})







