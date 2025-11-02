# # config/urls.py
# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("", include("apps.core.urls")),
#     # path("users/", include("apps.users.urls")),
#     path("portfolio/", include("apps.portfolio.urls")),
#     path("bookings/", include("apps.bookings.urls")),
#     path("proofing/", include("apps.proofing.urls")),
#     path("shop/", include("apps.ecommerce.urls")),
#     path("api/users/", include("apps.users.urls")),
#     path("api/users/", include("apps.users.urls")),
#     path("api/gallery/", include("apps.gallery.urls")),
#     path("api/contact/", include("apps.contact.urls")),
#     path('api/', include('apps.gallery.urls')),
#     # API endpoints could live under 'api/' using DRF
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.core.urls")),
    path("portfolio/", include("apps.portfolio.urls")),
    path("bookings/", include("apps.bookings.urls")),
    path("proofing/", include("apps.proofing.urls")),
    path("ecommerce/", include("apps.ecommerce.urls")),
    path("blog/", include("apps.blog.urls")),
    # path("users/", include("apps.users.urls")),
    path('users/', include(('apps.users.urls', 'users'), namespace='users')),
    # path("shop/", include("apps.ecommerce.urls")),
    path("api/users/", include("apps.users.urls")),
    path("api/gallery/", include("apps.gallery.urls")),
    path("api/contact/", include("apps.contact.urls")),
    path("api/", include("apps.gallery.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path("admin/", admin.site.urls),

#     # ✅ Homepage & core views
#     path("", include("apps.core.urls")),

#     # ✅ Other apps
#     path("portfolio/", include("apps.portfolio.urls")),
#     path("bookings/", include("apps.bookings.urls")),
#     path("proofing/", include("apps.proofing.urls")),
#     path("shop/", include("apps.ecommerce.urls")),
#     path("api/users/", include("apps.users.urls")),
#     path("api/gallery/", include("apps.gallery.urls")),
#     path("api/contact/", include("apps.contact.urls")),
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
