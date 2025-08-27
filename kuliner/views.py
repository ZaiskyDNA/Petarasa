from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import LokasiKuliner, Ulasan, JalurRasa
from django.db.models import Q

def peta_utama(request):
    context = {
        'active_page': 'peta'
    }
    return render(request, 'kuliner/peta.html', context)

def get_lokasi_json(request):
    query = request.GET.get('q', '')
    area = request.GET.get('area', '')

    lokasi_list = LokasiKuliner.objects.all()

    if query:
        lokasi_list = lokasi_list.filter(
            Q(nama__icontains=query) | Q(deskripsi__icontains=query)
        )
    if area:
        lokasi_list = lokasi_list.filter(area=area)

    data = []
    for lokasi in lokasi_list:
        foto_url = ''
        if lokasi.foto_utama:
            foto_url = lokasi.foto_utama.url

        data.append({
            'id': lokasi.id,
            'nama': lokasi.nama,
            'latitude': lokasi.latitude,          
            'longitude': lokasi.longitude,        
            'foto_url': foto_url,
            'is_produk_lokal': lokasi.is_produk_lokal, 
            'is_resep_asli': lokasi.is_resep_asli,      
        })
    return JsonResponse(data, safe=False)

# --- FUNGSI INI YANG DIUBAH ---
def detail_lokasi(request, pk):
    lokasi = get_object_or_404(LokasiKuliner, pk=pk)

    # Menambahkan atribut baru ke objek 'lokasi' untuk menyimpan
    # koordinat dalam format string dengan titik (.) sebagai desimal.
    # Ini adalah format yang aman untuk URL Google Maps.
    lokasi.latitude_str = str(lokasi.latitude)
    lokasi.longitude_str = str(lokasi.longitude)

    context = {
        'lokasi': lokasi,
        'active_page': 'peta' 
    }
    return render(request, 'kuliner/detail_lokasi.html', context)
# --- BATAS AKHIR PERUBAHAN ---

def tambah_ulasan(request, pk):
    lokasi = get_object_or_404(LokasiKuliner, pk=pk)
    if request.method == 'POST':
        nama = request.POST.get('nama_pengulas')
        rating = request.POST.get('rating')
        komentar = request.POST.get('komentar')

        try:
            if nama and rating and 1 <= int(rating) <= 5: 
                Ulasan.objects.create(
                    lokasi=lokasi,
                    nama_pengulas=nama,
                    rating=rating,
                    komentar=komentar
                )
        except (ValueError, TypeError):
            pass
            
    return redirect('detail-lokasi', pk=lokasi.pk)

def daftar_jalur_rasa(request):
    jalur_list = JalurRasa.objects.prefetch_related('lokasi').all()
    context = {
        'jalur_list': jalur_list,
        'active_page': 'jalur_rasa'
    }
    return render(request, 'kuliner/daftar_jalur_rasa.html', context)

def halaman_saran(request):
    context = {
        'active_page': 'saran'
    }
    return render(request, 'kuliner/halaman_saran.html', context)