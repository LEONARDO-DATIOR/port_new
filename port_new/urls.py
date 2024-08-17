from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("site_port.urls")),
    path("admin/", admin.site.urls),
]