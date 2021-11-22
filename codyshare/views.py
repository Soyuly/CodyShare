from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from account.models import Account
from django.contrib import auth
import json
from django.http import JsonResponse
# Create your views here.


def main(request):
    return render(request, 'main.html')

@login_required
def main_login(request, user_id):
    user = get_object_or_404(Account, pk=user_id)
    if request.user.is_authenticated:
        print('성공')
        return render(request, 'main.html', {'user': user}) 

def mypage(request):
    return render(request, 'mypage.html')

def create(request):
    return render(request,'create.html')

def detail(request):
    return render(request,'detail.html')
