from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static
#from . import views

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', include('core.urls')),  # This line includes your core app's URLs
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
