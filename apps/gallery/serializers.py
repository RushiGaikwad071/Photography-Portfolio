from rest_framework import serializers
from .models import Photo, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]

class PhotoSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Photo
        fields = ["id", "title", "description", "image", "category", "is_featured", "created_at"]

from rest_framework import viewsets
from .models import Category, Photo
from .serializers import CategorySerializer, PhotoSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
