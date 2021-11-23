from typing import Type
from django.core.checks import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from account.models import Account
from .models import Post
from django.contrib import auth
import json
from django.http import JsonResponse
from .models import Post, Like,Reservation, Message
from datetime import date, datetime


# Create your views here.


def main(request):
   posts = Post.objects.all()
   return render(request, 'main.html', {'posts':posts}) 

@login_required
def main_login(request, user_id):
    posts = Post.objects.all()
    if request.method == "POST":
        print("필터들어감")
        gender = request.POST.get('gender','')
        cloth = request.POST.get('cloth','')
        word = request.POST.get('word','')
        print(gender, cloth, word)
        posts = posts.filter(gender__icontains = gender, cloth_type__icontains = cloth, title__icontains = word)
    user = get_object_or_404(Account, pk=user_id)
    if request.user.is_authenticated:
        print('성공')
        return render(request, 'main.html', {'user': user, 'posts':posts}) 


def mypage(request):
    user = request.user
    user_obj = Account.objects.get(id=user.id)
    sell_posts = Post.objects.filter(user_id=user.id) #내가 쓴 글
    rent_posts=Reservation.objects.filter(buyer_id=user_obj) #내가 예약/신청한 게시물 가져오기
    arr_sell=[]
    arr_confirm=[]
    #내가 쓴 판매 게시물 가져오기
    for sell_obj in sell_posts:
        get_post=Reservation.objects.get(post_id=sell_obj.id) #내가 쓴 게시물에 대한 예약 신청 가져오기
        if(get_post.state==0):
            arr_sell.append(get_post.buyer_id.nickname)
    for sell_obj in sell_posts:
        get_post=Reservation.objects.get(post_id=sell_obj.id)
        if(get_post.state==1):
            arr_confirm.append(get_post.buyer_id.nickname)
    likes = Like.objects.all()
    likes = likes.filter(user_id = user_obj)
    print(likes)
    return render(request, 'mypage.html', { 'user' : user_obj, 'likes' : likes, 'sell_posts' : sell_posts  ,'rent_posts':rent_posts,'arr_sell':arr_sell,'arr_confirm':arr_confirm })


def create(request):
    return render(request,'create.html')

def detail(request, post_id):
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

    # 대여중 구현
    rent_posts = Reservation.objects.filter(post_id = post).filter(state = 1) #해당 글에 대한 예약 모두 가져옴
    if(rent_posts.exists()):
        for rent_post in rent_posts:
            print("현재 유저:", request.user, rent_post.buyer_id.user)
            print("대여 신청 기간", rent_post.rent_start, rent_post.rent_end)
            # 만약 rent_post 중 승인 상태이고 오늘 대여 기간과 오늘이 겹친다면 대여중으로 표시
            today = datetime.today()
            if (rent_post.rent_start < today.strftime("%Y-%m-%d") < rent_post.rent_end):
                # 대여 중인데 로그인한 유저가 대여한 유저라면
                if(rent_post.buyer_id.user == request.user):
                    renting = 2
                # 아니라면 그냥 대여중 띄우고 submit disabled
                else:
                    renting = 1
                return render(request,'detail.html', {'post':post, 'already':already, 'renting': renting})

    #반납 구현
    

    return render(request,'detail.html', {'post':post, 'already':already })

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
        reservation.rent_start = request.POST['start']
        reservation.rent_end = request.POST['end']
        reservation.state=0
        reservation.save()   
    return render(request,'main.html')

def message(request, rid, post_id):
    print("message")
    post = Post.objects.get(id = post_id)
    me = Account.objects.get(id = request.user.id);
    messages = Message.objects.filter(post_id = post).filter(recieve_id = me)
    messages_send = Message.objects.filter(post_id = post).filter(send_id = me)
    if request.method == "POST":
        message = Message()
        target = request.POST.get('target')
        print(request.user.id)
        print(rid)
        if(request.user.id == rid):
            error = 1
            return render(request,'message.html',{'rid':rid,'post_id':post_id,'messages':messages, 'messages_send':messages_send, 'error': error})
        if(target!="판매자"):
            message.recieve_id = Account.objects.get(nickname = target)
        if(target == "판매자"): 
            message.recieve_id = Account.objects.get(id = rid)
        
        message.content = request.POST['content']
        message.send_id = Account.objects.get(id = request.user.id);
        message.post_id = Post.objects.get(id = post_id)
        message.save()
        print("성공")
    return render(request,'message.html',{'rid':rid,'post_id':post_id,'messages':messages, 'messages_send':messages_send})

def mobile(request):
    return render(request, "mobile.html")


def apply(request,apply_mem):
    buyer = Account.objects.get(nickname = apply_mem)
    get_post=Reservation.objects.get(buyer_id=buyer)
    if get_post.state==0:
        get_post.state=1 #1은 승인
    get_post.save()

    return redirect('/mypage')

