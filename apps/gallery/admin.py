from django.contrib import admin
from .models import Category, Photo

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("title", "photographer", "category", "is_featured", "created_at")
    list_filter = ("is_featured", "category", "created_at")
    search_fields = ("title", "description")
