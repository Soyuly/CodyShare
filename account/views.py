from django.shortcuts import render

# Create your views here.

def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')

def modify(request):
    return render(request,'modify.html')

