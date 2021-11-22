from django.contrib import admin
from .models import Post
from account.models import Account
# Register your models here.

admin.site.register(Account)
admin.site.register(Post)