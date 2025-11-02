from django.shortcuts import render, get_object_or_404, redirect
from apps.portfolio.models import Gallery
from .models import ProofingGallery

def proofing_view(request, slug):
    # If using apps.proofing.ProofingGallery:
    gallery = get_object_or_404(ProofingGallery, slug=slug)
    session_key = f"proof_access_{gallery.pk}"
    if gallery.password:
        if request.session.get(session_key):
            return render(request, "proofing/proofing_gallery.html", {"gallery": gallery})
        return redirect("proofing:proof_password", slug=slug)
    return render(request, "proofing/proofing_gallery.html", {"gallery": gallery})

def proof_password(request, slug):
    gallery = get_object_or_404(ProofingGallery, slug=slug)
    error = None
    if request.method == "POST":
        pw = request.POST.get("password")
        if pw == gallery.password:
            request.session[f"proof_access_{gallery.pk}"] = True
            return redirect("proofing:proofing_view", slug=slug)
        error = "Incorrect password."
    return render(request, "proofing/proofing_password.html", {"gallery": gallery, "error": error})
