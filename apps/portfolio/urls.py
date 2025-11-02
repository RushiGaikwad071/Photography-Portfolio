# # apps/portfolio/urls.py
# from django.urls import path
# from . import views

# app_name = "portfolio"

# urlpatterns = [
#     path("", views.gallery_list, name="gallery_list"),
#     path("photo/<slug:slug>/", views.photo_detail, name="photo_detail"),
#     path("gallery/<slug:slug>/", views.gallery_public, name="gallery_public"),
# ]


from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.gallery_list, name="gallery_list"),
    path("gallery/<slug:slug>/", views.gallery_detail, name="gallery_detail"),
    path("photo/<slug:slug>/", views.photo_detail, name="photo_detail"),
]
