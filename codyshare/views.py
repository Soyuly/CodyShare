from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'main.html')

def mypage(request):
    return render(request, 'mypage.html')

def create(request):
    return render(request,'create.html')

def detail(request):
    return render(request,'detail.html')
