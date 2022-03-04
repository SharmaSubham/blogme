
from django.shortcuts import render
from .models import Blog
from user.models import Profile
from .models import Tags
# Create your views here.
def Home(request):
  tags= Tags.objects.all()
  work= Blog.objects.all()
  latest_blog=Blog.objects.order_by('-upload')[:5]
  params={'work':work,'latest_blog':latest_blog,'tags':tags}
  return render(request,"main.html", params)

# view for author
def authors(request):
    author=Profile.objects.all()
    a_pms={'author':author}
    return render(request, "author.html",a_pms)

#view for signin page
def signin(request):
    return render(request,"newsignin.html")

#view for signin page
def signup(request):
    return render(request,"signup.html")

def Read(request,pk):
    post=Blog.objects.filter(id=pk).first()
    read={'post':post}
    return render(request,"read.html",read)