from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import LokasiKuliner, Ulasan, JalurRasa
from django.db.models import Q

def peta_utama(request):
    return render(request, 'kuliner/peta.html')

def get_lokasi_json(request):
    # Ambil parameter pencarian (jika ada)
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
        })
    return JsonResponse(data, safe=False)

def detail_lokasi(request, pk):
    lokasi = get_object_or_404(LokasiKuliner, pk=pk)
    return render(request, 'kuliner/detail_lokasi.html', {'lokasi': lokasi})

def tambah_ulasan(request, pk):
    lokasi = get_object_or_404(LokasiKuliner, pk=pk)
    if request.method == 'POST':
        nama = request.POST.get('nama_pengulas')
        rating = request.POST.get('rating')
        komentar = request.POST.get('komentar')

        if nama and rating:
            Ulasan.objects.create(
                lokasi=lokasi,
                nama_pengulas=nama,
                rating=rating,
                komentar=komentar
            )
    return redirect('detail-lokasi', pk=lokasi.pk)

def daftar_jalur_rasa(request):
    jalur_list = JalurRasa.objects.all()
    return render(request, 'kuliner/daftar_jalur_rasa.html', {'jalur_list': jalur_list})

def halaman_saran(request):
    return render(request, 'kuliner/halaman_saran.html')