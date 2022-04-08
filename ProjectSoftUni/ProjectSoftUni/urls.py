"""
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ProjectSoftUni.main_app.urls')),
    path('profile/', include('ProjectSoftUni.accounts_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
