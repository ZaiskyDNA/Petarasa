from django.contrib import admin
from django.urls import path, include
from django.conf import settings  
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kuliner.urls')),
]

# TAMBAHKAN BLOK KODE DI BAWAH INI
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)