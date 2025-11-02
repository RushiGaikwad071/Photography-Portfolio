# apps/portfolio/models.py
from django.db import models
from django.utils.text import slugify
from django.utils import timezone
# from .models import Photo, Category

class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Photo(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=270, unique=True, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")
    raw = models.ImageField(upload_to="photos/raw/%Y/%m/%d/", blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name="photos", blank=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    taken_at = models.DateTimeField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:240]
            slug = base
            i = 1
            while Photo.objects.filter(slug=slug).exists():
                slug = f"{base}-{i}"
                i += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=270, unique=True, blank=True)
    cover_image = models.ImageField(upload_to="gallery_covers/%Y/%m/%d/", blank=True, null=True)
    photos = models.ManyToManyField(Photo, blank=True)
    background_music = models.FileField(upload_to="gallery_music/%Y/%m/%d/", blank=True, null=True,
                                        help_text="Upload an MP3 file to play as background music")
    description = models.TextField(blank=True, help_text="Short story about this couple or event")
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:240]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



def gallery_list(request):
    qs = Photo.objects.all().order_by("-is_featured", "-created_at")
    category_slug = request.GET.get("category")
    categories = Category.objects.all()

    if category_slug:
        qs = qs.filter(categories__slug=category_slug)

    return render(
        request,
        "portfolio/gallery_list.html",
        {"photos": qs, "categories": categories, "selected_category": category_slug},
    )
