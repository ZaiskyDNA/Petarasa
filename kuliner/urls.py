from django.urls import path
from . import views

urlpatterns = [
    path('', views.peta_utama, name='peta-utama'),
    path('api/lokasi/', views.get_lokasi_json, name='get-lokasi-json'),
    path('lokasi/<int:pk>/', views.detail_lokasi, name='detail-lokasi'),
    path('lokasi/<int:pk>/tambah-ulasan/', views.tambah_ulasan, name='tambah-ulasan'), 
    path('jalur-rasa/', views.daftar_jalur_rasa, name='daftar-jalur-rasa'),
    path('saran/', views.halaman_saran, name='halaman-saran'),
    ]
