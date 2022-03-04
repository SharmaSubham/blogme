import email
from tkinter import CASCADE
from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,blank=True,null=True)
    email=models.EmailField(max_length=200, blank=True,null=True)
    user_name=models.CharField(max_length=200)
    short_intro=models.CharField(max_length=200,blank=True,null=True)
    Bio=models.TextField(blank=True,null=True)
    auth_image=models.ImageField(null=True,blank=True,upload_to='static/blogging/authors')
    instagram=models.CharField(max_length=200 , null=False)
    linkedin=models.CharField(max_length=200 , null=False)
    snap_chat=models.CharField(max_length=200 , null=True)
    github=models.CharField(max_length=200 , null=False)
    sign_up=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)


    class Meta:
        ordering=['sign_up']

    def __str__(self):
        return self.user_name                 