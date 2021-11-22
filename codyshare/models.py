from django.db import models
from django.db.models.fields import CharField, DateField, IntegerField
from django.db.models.fields.files import ImageField

# Create your models here.
class Post(models.Model):
    title = CharField(max_length=200)
    content = CharField(max_length=500)
    img = ImageField()
    category1 = CharField(max_length=20)
    category2 = CharField(max_length=20)
    size = IntegerField()
    start = DateField(auto_now=True)
    end = DateField(auto_now=True)
    fee = IntegerField()   
