# apps/ecommerce/models.py
from django.db import models
from apps.portfolio.models import Photo
from django.conf import settings

class Product(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)
    price_cents = models.PositiveIntegerField()
    sku = models.CharField(max_length=80, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField()
    total_cents = models.PositiveIntegerField()
    stripe_session_id = models.CharField(max_length=255, blank=True, null=True)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
