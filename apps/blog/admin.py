from django.contrib import admin
from .models import BlogPost, Category

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created_at", "is_featured")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
