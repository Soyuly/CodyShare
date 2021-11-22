from django.core.checks import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from account.models import Account
from .models import Post
from django.contrib import auth
import json
from django.http import JsonResponse
from .models import Post, Like,Reservation, Message


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
    sell_posts = Post.objects.filter(user_id=user.id)
    
    likes = Like.objects.all()
    likes = likes.filter(user_id = user_obj)
    print(likes)
    return render(request, 'mypage.html', { 'user' : user_obj, 'likes' : likes, 'posts' : posts, 'sell_posts' : sell_posts   })


def create(request):
    return render(request,'create.html')

def detail(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    like = request.GET.get("like")
    
    if(request.GET.get("message")):
        rid = post.user_id.id
        print(post.user_id.id)
        return redirect('/message/' + str(post_id) + '/' + str(rid))

    already = Like.objects.all()
    if(request.user.id):
        user_id = Account.objects.get(id = request.user.id)
        already = already.filter(post= post)
        already = already.filter(user_id = user_id)
    if(like):
        if already : 
            already.delete()
        else:
            like = Like()
            like.user_id = user_id
            like.post = post
            like.save()
           
            
        return redirect('/detail/' + str(post_id))
    return render(request,'detail.html', {'post':post, 'already':already})

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



def rent(request):
    user = request.user
    reservation = Reservation()
    if request.method == "POST":
        reservation.buyer_id = Account.objects.get(id = user.id)
        reservation.post_id = Post.objects.get(id = request.POST['post_id'])
        reservation.rent_start = request.POST['rent_start']
        reservation.rent_end = request.POST['rent_end']
        reservation.state=0
        reservation.save()   
    return render(request, 'mypage.html')

def message(request, rid, post_id):
    print("message")
    post = Post.objects.get(id = post_id)
    me = Account.objects.get(id = request.user.id);
    messages = Message.objects.filter(post_id = post).filter(recieve_id = me)
    messages_send = Message.objects.filter(post_id = post).filter(send_id = me)
    if request.method == "POST":
        message = Message()
        message.content = request.POST['content']
        message.recieve_id = Account.objects.get(id = rid)
        message.send_id = Account.objects.get(id = request.user.id);
        message.post_id = Post.objects.get(id = post_id)
        message.save()
        print("성공")
    return render(request,'message.html',{'rid':rid,'post_id':post_id,'messages':messages, 'messages_send':messages_send})

