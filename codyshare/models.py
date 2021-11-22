from django.db import models
from django.db.models.fields import BooleanField, CharField, DateField, IntegerField
from django.db.models.fields.files import ImageField
from account.models import Account

# Create your models here.
class Post(models.Model):
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = CharField(max_length=200)
    content = CharField(max_length=500)
    img = ImageField(upload_to="img/")
    gender = CharField(max_length=20)
    cloth_type = CharField(max_length=20)
    size = CharField(max_length=10)
    start = DateField(auto_now=True)
    end = DateField(auto_now=True)
    fee = IntegerField()
    state=BooleanField(default=0)

class Like(models.Model):
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Reservation(models.Model):
    buyer_id=models.ForeignKey(Account, on_delete=models.CASCADE)
    post_id=models.ForeignKey(Post, on_delete=models.CASCADE)
    rent_start=CharField(max_length=200)
    rent_end=CharField(max_length=200)
    state=IntegerField(default=1)

