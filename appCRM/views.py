from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        users = authenticate(request, username=username, password=password)
        if users is not None:
            login(request, users)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.success(request, "There was an error, please try again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {})


def login_user(request):
    pass


def logout_user(request):
    pass
