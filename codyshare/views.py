from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from account.models import Account
from .models import Post
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
    user = request.user
    user_obj = Account.objects.get(id=user.id)

    # posts = Post.objects.all()
    posts = Post.objects.filter(user_id=user.id)

    return render(request, 'mypage.html', { 'user' : user_obj }, { 'posts' : posts })

def create(request):
    return render(request,'create.html')

def detail(request,post_id):
    return render(request,'detail.html')

def create_backend(request):
    user = request.user
    post = Post()
    if request.method == "POST":
        post.user_id = Account.objects.get(id = user.id)
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.img = request.FILES['img']
        post.gender = request.POST['gender']
        post.cloth_type = request.POST['cloth_type']
        post.size = request.POST['size']
        post.start = request.POST['start']
        post.end = request.POST['end']
        post.fee = request.POST['fee']
        post.save()   
    return redirect('/detail/' + str(post.id))