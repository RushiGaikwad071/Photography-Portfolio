# from django.urls import path
# from . import views

# app_name = "core"

# urlpatterns = [
#     # path("", views.home, name="home"),
#     path("about/", views.about, name="about"),
#     path("", home_view, name="home"),
# ]


from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact_view, name="contact"),
]


# from django.urls import path
# from .views import home_view

# app_name = "core"

# urlpatterns = [
#     path("", home_view, name="home"),
# ]
