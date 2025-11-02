# apps/bookings/admin.py
from django.contrib import admin
from .models import Booking, Package

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ("name", "price_cents", "duration_minutes")

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("client_name", "date", "time", "confirmed")
    list_filter = ("confirmed",)
    search_fields = ("client_name", "client_email")
