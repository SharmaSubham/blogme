from django.contrib import admin

from .models import  Tags
from .models import Blog
admin.site.register(Blog)

admin.site.register(Tags)

