from django.core.checks import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from account.models import Account
from django.contrib import auth
import json
from django.http import JsonResponse
from .models import Post, Like
# Create your views here.


def main(request):
   posts = Post.objects.all()
   return render(request, 'main.html', {'posts':posts}) 

@login_required
def main_login(request, user_id):
    user = get_object_or_404(Account, pk=user_id)
    posts = Post.objects.all()
    if request.user.is_authenticated:
        print('성공')
        return render(request, 'main.html', {'user': user, 'posts':posts}) 


def mypage(request):
    user = request.user
    user_obj = Account.objects.get(id=user.id)
    likes = Like.objects.all()
    likes = likes.filter(user_id = user_obj)
    print(user_obj)
    return render(request, 'mypage.html', { 'user' : user_obj, 'likes' : likes })

def create(request):
    return render(request,'create.html')

def detail(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    like = request.GET.get("like")

    already = Like.objects.all()
    if(request.user.id):
        user_id = Account.objects.get(id = request.user.id)
        already = already.filter(post= post)
        already = already.filter(user_id = user_id)
    if(like):
        if already : 
            messages.Error(request, "이미 스크랩한 게시글 입니다.")
        else:
            like = Like()
            like.user_id = user_id
            like.post = post
            like.save()
           
            
        return redirect('/detail/' + str(post_id))
    return render(request,'detail.html', {'post':post})

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

    # def like(request):
    #     user_obj = request.user
    #     likes = Like.objects.all()
    #     likes = likes.filter(user_id = user_obj)
    #     return render