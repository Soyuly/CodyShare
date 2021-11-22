from django.db import models
from django.db.models.fields import CharField, DateField, IntegerField
from django.db.models.fields.files import ImageField
from account.models import Account

# Create your models here.
class Post(models.Model):
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = CharField(max_length=200)
    content = CharField(max_length=500)
    img = ImageField()
    gender = CharField(max_length=20)
    cloth_type = CharField(max_length=20)
    size = CharField(max_length=10)
    start = DateField(auto_now=True)
    end = DateField(auto_now=True)
    fee = IntegerField()
