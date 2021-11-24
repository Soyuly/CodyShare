from django.shortcuts import render, redirect, get_object_or_404
from .models import Account
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError


# Create your views here.


def login(request):
    return render(request, 'login.html')


def login_backend(request):
    username = request.POST['id']
    password = request.POST['password']
    user = auth.authenticate(request, username=username, password=password)
    if user is not None:
        auth.login(request, user)
        print(user.id)
        return redirect('main/'+str(request.user.id))
    else:
        error = 1
        print(error)
        return render(request, 'login.html', {'error': error})


def logout_backend(request):
    auth.logout(request)
    return redirect('main_logout')


def signup(request):
    return render(request, 'signup.html')


def signup_backend(request):

    if request.method  == 'POST':
        account = Account()
        account.photo = request.FILES['photo']
        account.nickname = request.POST['nickname']
        account.birth = request.POST['birth']
        account.gender = request.POST['gender']
        account.name = request.POST['name']
        account.address = request.POST['location']

        print('회원가입')
        if User.objects.filter(username=request.POST['id']).exists():
            error = 1
            return render(request, 'signup.html', {'error': error})
            
        account.user = User.objects.create_user(
        username=request.POST['id'], password=request.POST['password'])
        account.save()
     
    user = auth.authenticate(
        request, username=request.POST['id'], password=request.POST['password'])

    if account is not None:
        auth.login(request, user)
        return redirect('/main/'+str(request.user.id))
    else:
        error = 1
        return render(request, 'login.html', {'error': error})


def edit_account_backend(request, user_id):
    user = get_object_or_404(Account, pk=user_id)
    if request.method == "POST":
        user.name = request.POST['name']
        user.nickname = request.POST['nickname']
        user.major = request.POST['major']
        user.birth = request.POST['birth']
        user.gender = request.POST['gender']
        user.save()
    return redirect('/mypage/'+str(user_id))


def edit_account(request, user_id):
    user = get_object_or_404(Account, pk=user_id)
    return render(request, 'edit_account.html', {'user': user})

def modify(request):
    return render(request, 'modify.html')


def map(request):
    return render(request, 'map.html')


def mapvalue(request):
    print("값",request.POST['address'])
    if request.method == "POST":
        located=request.POST['address']
    return render(request,'signup.html',{'located':located})

def mapvalue_kakao(request):
    print("값",request.POST['address'])
    if request.method == "POST":
        located=request.POST['address']
    return redirect('/kakao')

class KakaoException:
    pass

def kakao_login(request):
    client_id = 'eebc5ddba4a23626be8715744818895c'
    REDIRECT_URI = "http://127.0.0.1:8000/kakao/callback"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={REDIRECT_URI}&response_type=code"
    )
def kakao_callback(request):
    	#카카오 회원가입 과정
    code = request.GET.get("code")
    client_id = "eebc5ddba4a23626be8715744818895c"
    REDIRECT_URI = "http://127.0.0.1:8000/kakao/callback"
    #(2)
    token_request = requests.get(
        f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={REDIRECT_URI}&code={code}"
    )
    token_json = token_request.json()
    error = token_json.get("error", None)

    access_token = token_json.get("access_token")

    # 카카오 프로필 정보를 받아온다.
    profile_request = requests.get(
        "https://kapi.kakao.com/v2/user/me",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    profile_json = profile_request.json()


    #카카오 프로필 정보
    email = profile_json.get("kakao_account", None).get("email") #이메일
    if email is None:
        raise KakaoException()
    properties = profile_json.get("properties") 
    nickname = properties.get("nickname") #닉네임
    profile_image = properties.get("profile_image") #프로필 이미지
    gender = profile_json.get("kakao_account", None).get("gender")
    userid = profile_json.get("id")

    # 만약 계정이 있으면
    if User.objects.filter(username=userid).exists():
        user = auth.authenticate(request, username=userid, password="1234567")   
        auth.login(request, user)
        return redirect('/main/'+str(request.user.id))
    print(userid)
    #(7)
    account = Account()
    
    account.photo = profile_image
    account.nickname = nickname
    account.name = nickname
    account.address = "진주시 가좌동"
    account.gender = gender
    account.birth = ''

    print('회원가입')

    
    account.user = User.objects.create_user(
        username=userid, password="1234567")
    account.save()
    print("회원가입 성공")
    user = auth.authenticate(
        request, username=userid, password="1234567")

    if account is not None:
        print("로그인 성공")
        auth.login(request, user)
        return redirect('/main/'+str(request.user.id))
    else:
        error = 1
        return render(request, 'login.html', {'error': error})
    
    