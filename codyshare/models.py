from django.db import models
from django.db.models.fields import BooleanField, CharField, DateField, IntegerField
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
    state=BooleanField(default=0)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def sum_content(self):
        return self.content[:20]


class Like(models.Model):
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def sum_content(self):
        return self.content[:20]
    
class Reservation(models.Model):
    buyer_id=models.ForeignKey(Account, on_delete=models.CASCADE)
    post_id=models.ForeignKey(Post, on_delete=models.CASCADE)
    rent_start=CharField(max_length=200)
    rent_end=CharField(max_length=200)
    state=IntegerField(default=1)
    
    def sum_content(self):
        return self.content[:20]

class Message(models.Model):
    send_id = models.ForeignKey(Account, on_delete=models.CASCADE,  related_name= 'send' )
    recieve_id = models.ForeignKey(Account, on_delete=models.CASCADE,  related_name= 'recieve' )
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    
    def sum_content(self):
        return self.content[:20]

