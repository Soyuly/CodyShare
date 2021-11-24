from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    photo = models.ImageField(upload_to="profile/")
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    nickname = models.CharField(max_length=100)
    name = models.CharField(max_length=10)
    address = models.TextField()
    birth = models.CharField(max_length=15)
    gender = models.CharField(max_length=5)
    # def str(self):
    #     return self.user.id
