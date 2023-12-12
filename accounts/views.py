from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.urls import reverse
# Create your views here.

from django.http import HttpResponse

def accounts(request):
    return HttpResponse("Hello, this is the accounts page.")



def register(request):
    if request.method == "POST":
        username = request.POST['User_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('Register')
        if User.objects.filter(username = username).exists():
            messages.info(request,"username taken")
            return redirect('Register')
        elif User.objects.filter(email = email).exists():
            messages.info(request, "email  exists")
            return redirect('Register')

        else:
            user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.save()

        messages.success(request, 'Account created successfully. You can now log in.')
        return redirect('Login')

    return render(request,'registration.html')

def login(request):
    if request.method == "POST":
        username = request.POST['User_name']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid details')
    else:
        return render(request,'Login.html')

def logout(request):
    auth.logout(request)
    return redirect(reverse('Login'))