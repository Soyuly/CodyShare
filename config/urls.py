"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from codyshare import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main, name="main_logout"),
    path('main/<str:user_id>', views.main_login, name='main'),
    path('apply/<str:apply_mem>', views.apply, name='apply'),
    path('return_item/<str:return_item>', views.return_item, name='return_item'),
    path('mypage', views.mypage, name="mypage"),
    path('rent/<str:user_id>', views.rent, name="rent"),
    
    path('', include('account.urls')), 
    path('create/',views.create, name="create"),
    path('detail/<str:post_id>',views.detail, name="detail"),
    path('create_backend/',
         views.create_backend, name='create_backend'),    
    path('message/<str:post_id>/<str:rid>', views.message, name="message"),
     path('mobile/', views.mobile, name='mobile'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
