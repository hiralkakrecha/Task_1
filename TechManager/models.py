from django.db import models
from django.conf import settings
from django.db import models
# Create your models here.


class Blog(models.Model):
    blog_link = models.CharField(max_length=150)
    blog_image = models.ImageField(upload_to = "blog/images", default="")
    blog_content = models.CharField(max_length = 2000)

    def save(self, *args, **kwargs):
       return super().save(*args, **kwargs)

