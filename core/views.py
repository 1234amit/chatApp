from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages


# Create your views here.
def frontPage(request):
    return render(request, 'core/frontpage.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('frontPage')
        
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authentication
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been Logged In")
            return redirect('frontPage')
        else:
            messages.success(request, "There is a problem for login. please Try again")
            return redirect('login')
    else:
        return render(request, 'core/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect("signup")
