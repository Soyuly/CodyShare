from django.db import models
from django.db.models.fields import CharField, DateField, IntegerField
from django.db.models.fields.files import ImageField
from account.models import Account
from datetime import datetime

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
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def sum_content(self):
        return self.content[:20]

# class GiveBack(models.Model):
#     seller = models.ForeignKey(Account, on_delete=models.CASCADE)
#     buyer = models.ForeignKey(Account, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)