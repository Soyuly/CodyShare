from django.contrib import admin
from .models import Post,Like
from account.models import Account
# Register your models here.

admin.site.register(Account)
admin.site.register(Post)
admin.site.register(Like)