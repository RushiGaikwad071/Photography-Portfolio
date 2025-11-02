from django.shortcuts import render, redirect
from .forms import BookingForm

def book(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            # optionally send email to admin - omitted for brevity
            return redirect("bookings:book_success")
    else:
        form = BookingForm()
    return render(request, "bookings/booking_form.html", {"form": form})

def book_success(request):
    return render(request, "bookings/booking_success.html")
