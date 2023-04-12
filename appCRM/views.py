from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecord
from .models import Record


# Create your home views here.
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


# Create your logout views here.
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')


# Create your register views here.
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


# Create your customization  views here.
def customize_record(request, pk):
    if request.user.is_authenticated:
        custo_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {"custo_record": custo_record})

    else:
        messages.success(request, "You must be logged in")
        return redirect('home')


# here is the view to delete individual record
def delete_record(request, pk):
    if request.user.is_authenticated:
        delet_record = Record.objects.get(id=pk)

        if request.method == 'POST':
            delet_record.delete()
            messages.success(request, "Deleted successfully")
            return redirect('home')
        return render(request, 'delete_item.html', {'delet_record': delet_record})
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')


# the add new record view is goes here
def add_record(request):
    form = AddRecord(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, " Record saved successfully")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, " You must be logged in")
        return redirect('home')


# the update record view section
def update_record(request, pk):
    current_record = Record.objects.get(id=pk)
    form = AddRecord(request.POST or None, instance=current_record)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, " Record has been updated")
                return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, " You must be logged in")
        return redirect('home')
