from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record


# Create your views here.
def index(request):
    records = get_list_or_404(Record)

    # check to see if logging in (POST)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in!")
            return redirect("index")
        else:
            messages.error(request, "There was an error logging in, pls try again")
            return redirect("index")
    # just viewing the page (GET)
    else:
        return render(request, 'index.html', {'records': records})


def user_login(request):
    pass


def user_logout(request):
    logout(request)
    messages.success(request, "You have logged out.")
    return redirect("index")


def user_reg(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # auth and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully Registered!")
                return redirect("index")
            else:
                messages.error(request, "There was an error logging in, pls try again")
                return redirect("index")
    else:
        form = SignUpForm()
        return render(request, 'reg.html', {'form': form})
    return render(request, 'reg.html', {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        # record = get_object_or_404(Record, id=pk)
        record = get_object_or_404(Record, pk=pk)
        return render(request, 'record.html', {'record': record})
    else:
        messages.success(request, "You must be logged in...")
        return redirect("index")


def record_delete(request, pk):
    if request.user.is_authenticated:
        record = get_object_or_404(Record, pk=pk)
        record.delete()
        messages.success(request, "Record deleted successfully")
        return redirect("index")
    else:
        messages.success(request, "You must be logged in...")
        return redirect("index")


def record_create(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                # add record
                form.save()
                messages.success(request, "record saved")
                return redirect("index")
        return render(request, 'records/create.html', {'form': form})
    messages.success(request, "You must be logged in...")
    return redirect("index")


def record_update(request, pk):
    if request.user.is_authenticated:
        record = get_object_or_404(Record, pk=pk)
        form = AddRecordForm(request.POST or None, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "record updated")
            return redirect("index")
        return render(request, 'records/update.html', {'form': form})
    messages.success(request, "You must be logged in...")
    return redirect("index")
