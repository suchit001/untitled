from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from . import views



urlpatterns = [
    path('',views.home),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('tinymce/',include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)