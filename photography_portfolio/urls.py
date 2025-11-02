"""
URL configuration for photography_portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path,include
# from apps.categories.views import CategoryViewSet

# router.register(r'categories', CategoryViewSet)

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("api/users/", include("apps.users.urls")),
#     path("api/gallery/", include("apps.gallery.urls")),
#     path("api/contact/", include("apps.contact.urls")),
#     path("api/category/", include("apps.category.urls")),
# ]


# from django.contrib import admin
# from django.urls import path, include
# from rest_framework import routers

# # Import your viewsets
# from apps.users.views import UserViewSet
# from apps.gallery.views import PhotoViewSet
# from apps.contact.views import ContactViewSet
# from apps.categories.views import CategoryViewSet

# # Create the router instance
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'gallery', PhotoViewSet)
# router.register(r'contact', ContactViewSet)
# router.register(r'categories', CategoryViewSet)  # ✅ Added correctly here

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include(router.urls)),  # ✅ Include all API routes
# ]



from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    # 👇 homepage and about page
    path("", include("apps.core.urls")),

    # 👇 other apps
    path("portfolio/", include("apps.portfolio.urls")),
    path("bookings/", include("apps.bookings.urls")),
    path("proofing/", include("apps.proofing.urls")),
    path("shop/", include("apps.ecommerce.urls")),
    path("api/users/", include("apps.users.urls")),
    path("api/gallery/", include("apps.gallery.urls")),
    path("api/contact/", include("apps.contact.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




