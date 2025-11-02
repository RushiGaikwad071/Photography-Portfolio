from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PhotoViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r"photos", PhotoViewSet)
router.register(r"categories", CategoryViewSet)

urlpatterns = [path("", include(router.urls))]
