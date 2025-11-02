# from django.urls import path
# from . import views

# app_name = "users"

# urlpatterns = [
#     path("", views.profile, name="profile"),
#     path("", views.UserListView.as_view(), name="user-list"),
# ]

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import UserViewSet

# router = DefaultRouter()
# router.register(r"users", UserViewSet)

# urlpatterns = [path("", include(router.urls))]

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import UserViewSet
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

# router = DefaultRouter()
# router.register(r"users", UserViewSet)

# urlpatterns = [
#     path("", include(router.urls)),
#     path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
#     path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
# ]


# apps/users/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'users'
router = DefaultRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
