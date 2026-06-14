from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/service/", include("characters.urls", namespace="characters")),
]
