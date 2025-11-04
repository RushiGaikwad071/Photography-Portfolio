from django.shortcuts import render, get_object_or_404
from .models import Photo, Gallery

def gallery_list(request):
    qs = Photo.objects.all().order_by("-is_featured", "-created_at")
    category = request.GET.get("category")
    if category:
        qs = qs.filter(categories__slug=category)
    return render(request, "portfolio/gallery_list.html", {"photos": qs})

def photo_detail(request, slug):
    p = get_object_or_404(Photo, slug=slug)
    return render(request, "portfolio/photo_detail.html", {"photo": p})

def gallery_detail(request, slug):
    g = get_object_or_404(Gallery, slug=slug)
    return render(request, "portfolio/gallery_detail.html", {"gallery": g})

def portfolio_view(request):
    """Portfolio page showing all galleries"""
    galleries = Gallery.objects.all().order_by("-created_at")
    return render(request, "portfolio/portfolio.html", {"galleries": galleries})

def gallery_detail(request, slug):
    """Gallery detail page showing photos inside one gallery"""
    gallery = get_object_or_404(Gallery, slug=slug)
    photos = gallery.photos.all().order_by("-created_at")
    return render(request, "portfolio/gallery_detail.html", {
        "gallery": gallery,
        "photos": photos,
    })