from distutils.command.upload import upload
from operator import truediv
from pyexpat import model
from tkinter.messagebox import RETRY
import uuid
from django.db import models
from user.models import Profile
# Create your models here.






class Blog(models.Model):
    # object=models.CharField
    blog_title=models.CharField( max_length=70 ,null=False)
    user_name= models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE )
    image = models.ImageField(upload_to="static/blogging/images", default="")
    Quote=models.TextField(max_length=2000, default="")
    upload=models.DateTimeField()
    short_intro=models.TextField(max_length=220 ,default="")
    tags =models.ManyToManyField("Tags", related_name="tag")
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    class Meta:
        ordering=['upload']
        
    def __str__(self):
        return self.blog_title

class Tags(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    class Meta:
        ordering=['name']

    def __str__(self):
        return self.name