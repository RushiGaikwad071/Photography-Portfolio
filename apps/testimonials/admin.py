from django.contrib import admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "rating", "location", "is_featured", "created_at")
    list_filter = ("is_featured", "rating", "created_at")
    search_fields = ("name", "short_message", "full_message", "location")
    prepopulated_fields = {"slug": ("name",)}
