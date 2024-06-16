from django.shortcuts import redirect, render
from .forms import LoginForm, UserRegistartionForm
from django.contrib.auth import authenticate, login

  
def invalid(request, message):
    return render(request, 'todo/invalid.html', {"message": message})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistartionForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('login')
    else:
        user_form = UserRegistartionForm()
    return render(request, 'todo/register.html', {'user_form': user_form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return redirect('invalid', message='Incorrect password')
    else:
        form = LoginForm()
    return render(request, 'todo/login.html', {'form': form})
 