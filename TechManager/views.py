from django.shortcuts import render
from rest_framework.views import APIView
from TechManager import models

# Create your views here.

class BlogView(APIView):
    def get(self, request):
        allblog = models.Blog.objects.all()
        list1 = []
        for blog in allblog:
            list1.append(blog)
        context = {
            'blog_data':list1
        }    
        return render(request,'index.html', context)

