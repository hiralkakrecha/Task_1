from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Blog

# Register your models here.

# @admin.register(Blog)
# class BlogModelAdmin(admin.ModelAdmin):
#     list_display = ['id','blog_link','blog_image','blog_content']

class BlogModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Blog
    list_display = ['blog_link','blog_image','blog_content']
admin.site.register(Blog,BlogModelAdmin)