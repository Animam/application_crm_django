from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record
from django.views.decorators.http import require_POST


# Create your views here.
def home(request):
    # check if the user is logged in
    record = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # authenticate
        users = authenticate(request, username=username, password=password)
        if users is not None:
            login(request, users)
            messages.success(request, "You have logged in successfully")
            return redirect('home')
        else:
            messages.success(request, "There was an error, please try again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {'record': record})


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "You have been registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})


def customize_record(request, pk):
    if request.user.is_authenticated:
        custo_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {"custo_record": custo_record})

    else:
        messages.success(request, "You must be logged in")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delet_record = Record.objects.get(id=pk)
        if request.method == 'POST':
            delet_record.delete()
            messages.success(request, "Deleted successfully")
            return redirect('home')
        return render(request, 'delete_item.html')
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')
