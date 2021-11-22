from django.contrib import admin
from .models import Post,Like,Reservation
from account.models import Account
# Register your models here.
admin.site.register(Reservation)
admin.site.register(Account)
admin.site.register(Post)
admin.site.register(Like)