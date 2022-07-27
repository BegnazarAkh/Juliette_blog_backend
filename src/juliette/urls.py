from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .views import *

from juliette.settings import STATIC_ROOT, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('listing1/', listing1),
    path('listing2/', listing2),
    path('post/', post),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   
