from distutils.command.upload import upload
from operator import truediv
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
import uuid
from user.models import Profile



class Blog(models.Model):
    Author=models.ForeignKey(Profile,on_delete=models.CASCADE)
    blog=models.TextField()
    blog_title=models.CharField(max_length=33)
    desc=models.CharField(max_length=100, null=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    blog_image=models.ImageField(null=True,blank=True,upload_to='static/blogging/images')
    Pen_name=models.CharField(max_length=7)
    insta=models.CharField(max_length=20, blank=True)
    linkedin=models.CharField(max_length=9,blank=True)
    upload=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['upload']

    def __str__(self):
        return self.blog_title    

class Tags(models.Model):
    name=models.CharField(max_length=9)
    created=models.DateTimeField(auto_now_add=TRUE)
    id=models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
   
    class Meta:
        ordering=['created']

    def __str__(self):
        return self.name 