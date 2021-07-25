from django.shortcuts import render

# Create your views here.

def user(request):
    return render(request,"users/user.html")

def user_login(request):
    return render(request, "users/user_login.html")    

def user_signup(request):
    return render(request, "users/user_signup.html")


