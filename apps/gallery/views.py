from rest_framework import viewsets, filters
from .models import Photo, Category
from .serializers import PhotoSerializer, CategorySerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PhotoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Photo.objects.all().select_related("category", "photographer")
    serializer_class = PhotoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "description", "category__name"]
    ordering_fields = ["created_at"]
