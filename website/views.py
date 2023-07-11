from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def index(request):
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
        return render(request, 'index.html', {})


def user_login(request):
    pass


def user_logout(request):
    logout(request)
    messages.success(request, "You have logged out.")
    return redirect("index")


def user_reg(request):
    return render(request, 'reg.html', {})
