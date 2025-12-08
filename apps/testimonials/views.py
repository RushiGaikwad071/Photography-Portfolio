from django.shortcuts import render, get_object_or_404
from .models import Testimonial

def testimonial_list(request):
    testimonials = Testimonial.objects.all()
    return render(request, "testimonials/testimonial_list.html", {"testimonials": testimonials})

def testimonial_detail(request, slug):
    testimonial = get_object_or_404(Testimonial, slug=slug)
    return render(request, "testimonials/testimonial_detail.html", {"testimonial": testimonial})
