from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from main_app.views import login_api

urlpatterns = (
    [
        path("", include("main_app.urls")),
        path("accounts/", include("django.contrib.auth.urls")),
        path("admin/", admin.site.urls),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
