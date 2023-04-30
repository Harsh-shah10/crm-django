from django.shortcuts import render, redirect

# django login logout modules
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Course
import re
from django.conf import settings

def homepage(request):
    # If the user is not logged in
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
    if request.method == 'GET':    
        records = Course.objects.all().order_by('course_name')
        return render(request, 'homepage.html', {'records': records})
    else:
        return render(request, 'homepage.html')
        
def user_login(request):
    pass

def user_register(request):
    if request.method == 'POST':            
        # Get data from request body
        Email = request.POST.get('Email')
        username = request.POST.get('Username')
        password1 = request.POST.get('Password1')
        password2 = request.POST.get('Password2')
        secret = request.POST.get('secret')
        
        if not secret:
            messages.success(request, "Pass secret Identity")
            return redirect('register')
        # Validate data
        if not Email:
            messages.success(request, "Email is required")
            return redirect('register')        
        if not username:
            messages.success(request, "Username is required")
            return redirect('register')
        if not password1:
            messages.success(request, "Password is required")
            return redirect('register')
        if not password2:
            messages.success(request, "Password and confirm password are required")
            return redirect('register')
        
        if password1 != password2:
            messages.success(request, "Password and confirm password must be same")
            return redirect('register')
        
        # validate form by usng regex pattern
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(regex, Email):
            messages.success(request, "Email is invalid")
            return redirect('register')
        
        regex = r'^(?=.*[a-zA-Z])[a-zA-Z0-9_-]{3,}$'
        if not re.match(regex, username):
            messages.success(request, "username is invalid")
            return redirect('register')
        
        regex = r'^[a-zA-Z0-9_\-@.*#?$&!%+={}\[\]~^()]{3,}$'
        if not re.match(regex, password1):
            messages.success(request, "Password is invalid")
            return redirect('register')
        
        if settings.SECRET_PASS != secret:
            messages.success(request, "Invalid secret key")
            return redirect('register')

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            messages.success(request, "Username already exists")
            return redirect('register')
        
        new_user = User(username=username, email=Email)
        # set the user's password
        new_user.set_password(password1)
        # save the user object to the database
        new_user.save()
        messages.success(request, "Account created successfully!")
        return render(request, 'homepage.html')
    else:
        return render(request, 'register.html')    

def user_logout(request):
    logout(request)
    messages.success(request, "User LoggedOut!")
    return render(request, 'homepage.html')
    
    