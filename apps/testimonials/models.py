from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="testimonials/", blank=True, null=True)
    message = models.TextField()
    rating = models.PositiveIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.rating}★)"



from django.db import models
from django.utils.text import slugify

class Testimonial(models.Model):
    couple_names = models.CharField(max_length=200, help_text="e.g. 'Viraj & Dhaval'")
    slug = models.SlugField(unique=True, blank=True)
    short_quote = models.TextField(help_text="1–2 line highlight.")
    full_quote = models.TextField(blank=True)
    image = models.ImageField(upload_to="testimonials/", blank=True, null=True)
    location = models.CharField(max_length=150, blank=True)
    wedding_date = models.DateField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-is_featured", "-created_at"]

    def __str__(self):
        return self.couple_names

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.couple_names)
        super().save(*args, **kwargs)
