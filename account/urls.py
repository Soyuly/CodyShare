from django.contrib import admin
from django.urls import path
from account import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('login_backend', views.login_backend, name='login_backend'),
    path('logout_backend', views.logout_backend, name='logout_backend'),
    path('signup/', views.signup, name='signup'),
    path('map/', views.map, name='map'),
    path('mapvalue', views.mapvalue, name='mapvalue'),
    path('signup_backend', views.signup_backend, name='signup_backend'),
    path('edit_account_backend/<str:user_id>', views.edit_account_backend,
         name='edit_account_backend'),
    path('edit_account/<str:user_id>', views.edit_account, name='edit_account'),
    path('kakao/login', views.kakao_login, name='kakao_login'),
    path('kakao/callback/', views.kakao_callback, name='kakao_callback'),


   
  
]