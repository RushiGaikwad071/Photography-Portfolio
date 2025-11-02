from django.urls import path
from . import views

app_name = "proofing"

urlpatterns = [
    path("<slug:slug>/", views.proofing_view, name="proofing_view"),
    path("<slug:slug>/password/", views.proof_password, name="proof_password"),
]
