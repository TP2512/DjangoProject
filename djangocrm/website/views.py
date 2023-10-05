from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def home(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            messages.success(request,"You Have Been Logged In")
            return redirect('home')
        else:
            messages.success(request,"There is an Error While logging in .Please try again........")
            return redirect('home')
    else:
        return render(request,'home.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out......")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})
