from django.urls import path
from . import views

app_name = "bookings"

urlpatterns = [
    path("book/", views.book, name="book"),
    path("success/", views.book_success, name="book_success"),
]
