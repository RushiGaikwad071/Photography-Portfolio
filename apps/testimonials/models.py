from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="testimonials/", blank=True, null=True)
    message = models.TextField()
    rating = models.PositiveIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.rating}★)"
