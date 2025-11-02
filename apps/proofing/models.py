# apps/proofing/models.py
from django.db import models
from apps.portfolio.models import Photo, Gallery as PortfolioGallery
from django.conf import settings

class ProofingGallery(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    photos = models.ManyToManyField(Photo, blank=True)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    password = models.CharField(max_length=128, blank=True, null=True)  # demo only
    created_at = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Feedback(models.Model):
    proofing = models.ForeignKey(ProofingGallery, on_delete=models.CASCADE, related_name="feedbacks")
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    liked = models.BooleanField(default=False)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
