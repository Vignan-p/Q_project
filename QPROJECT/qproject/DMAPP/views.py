from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request,'login.html')


def superadmin(request):
    return render(request,'superadmin.html')

def user(request):
    return render(request,'user.html')

def user_report(request):
    return render(request,'user_report.html')

def task_creation(request):
    return render(request,'task_creation.html')