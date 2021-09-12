from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('tarjimon.urls')),
    path('admin/', admin.site.urls),
]
