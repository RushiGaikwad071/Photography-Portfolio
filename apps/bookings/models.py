# apps/bookings/models.py
from django.db import models
from django.conf import settings

class Package(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price_cents = models.PositiveIntegerField(default=0)
    duration_minutes = models.IntegerField(default=60)

    def __str__(self):
        return self.name

class Booking(models.Model):
    client_name = models.CharField(max_length=200)
    client_email = models.EmailField()
    client_phone = models.CharField(max_length=50, blank=True)
    date = models.DateField()
    time = models.TimeField()
    
    # PACKAGE_CHOICES = [
    #     ("Wedding", "Wedding"),
    #     ("Pre-wedding", "Pre-Wedding"),
    #     ("post-wedding", "Post-Wedding"),
    #     ("model shoot", "Model Shoot"),
    #     ("portrait", "Portrait"),
    #     ("event", "Event"),
    #     ("product", "Product Shoot"),
    # ]
    # package = models.CharField(max_length=50, choices=PACKAGE_CHOICES)

    package = models.ForeignKey(Package, on_delete=models.CASCADE)

    location = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)
    assigned_photographer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.client_name} — {self.date} {self.time}"
