from django.shortcuts import render, redirect

# django login logout modules
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def homepage(request):
    if request.method == 'POST':
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')
        # auth logic 
        user = authenticate(request, username=Username, password=Password)
        if user:
            login(request, user)
            messages.success(request, "User logged in successfully !")
            return redirect('homepage')
        else:
            messages.success(request, "Invalid Username or Password !")
            return redirect('homepage')
    else:
        return render(request, 'homepage.html')
    
def user_login(request):
    pass

def user_logout(request):
    logout(request)
    messages.success(request, "User LoggedOut!")
    return render(request, 'homepage.html')
    
    