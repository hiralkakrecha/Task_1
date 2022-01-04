from rest_framework import serializers
from TechManager.models import Blog

class BlogSerializer(serializers.Serializer):
    blog_link = serializers.CharField(max_length=150, required=False)
    blog_image = serializers.ImageField()
    blog_content = serializers.CharField(max_length = 2000, required=False)

    def create(self, validated_data):
        return Blog.objects.create(**validated_data)