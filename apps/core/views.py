# from django.shortcuts import render
# from apps.portfolio.models import Photo

# # def home(request):
# #     featured = Photo.objects.filter(featured=True).order_by("-created_at")[:8]
# #     return render(request, "core/home.html", {"featured": featured})

# def about(request):
#     return render(request, "core/about.html")

# def home_view(request):
#     # Fetch featured photos (or latest if none marked)
#     featured = Photo.objects.filter(is_featured=True).order_by('-created_at')[:8]
#     if not featured.exists():
#         featured = Photo.objects.all().order_by('-created_at')[:8]

#     context = {
#         "featured": featured,
#     }
#     return render(request, "core/home.html", context)


# from django.shortcuts import render
# from apps.portfolio.models import Photo

# def home_view(request):
#     # Fetch featured photos (or latest if none marked)
#     featured = Photo.objects.filter(is_featured=True).order_by('-created_at')[:8]
#     if not featured.exists():
#         featured = Photo.objects.all().order_by('-created_at')[:8]

#     context = {
#         "featured": featured,
#     }
#     return render(request, "core/home.html", context)


# def about(request):
#     return render(request, "core/about.html")



from django.shortcuts import render, redirect
from django.contrib import messages

# Import models
from apps.portfolio.models import Photo, Gallery
from apps.testimonials.models import Testimonial
from apps.blog.models import BlogPost

# Import booking form
from apps.bookings.forms import BookingForm
from apps.bookings.models import Package


# Import contact form
from .forms import ContactForm


def home_view(request):
    """Render the dynamic homepage with featured content + booking section."""
    featured_photos = Photo.objects.filter(is_featured=True)[:6]
    galleries = Gallery.objects.all()[:4]
    testimonials = Testimonial.objects.all()[:3]
    latest_posts = BlogPost.objects.all()[:2]
    booking_form = BookingForm(request.POST or None)  # 👈 added this
    booking_form.fields["package"].queryset = Package.objects.all()
    if request.method == "POST" and booking_form.is_valid():
        booking_form.save()
        messages.success(request, "Your booking request has been submitted successfully!")
        return redirect("core:home")

    context = {
        "featured_photos": featured_photos,
        "galleries": galleries,
        "testimonials": testimonials,
        "latest_posts": latest_posts,
        "booking_form": booking_form,  # 👈 include in context
    }
    return render(request, "core/home.html", context)


def about(request):
    """About page."""
    return render(request, "core/about.html")


def contact_view(request):
    """Contact form page."""
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent! I’ll get back to you soon.")
            return redirect("core:contact")
    else:
        form = ContactForm()
    return render(request, "core/contact.html", {"form": form})
