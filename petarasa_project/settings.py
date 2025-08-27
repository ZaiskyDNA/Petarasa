import os
import dj_database_url
from dotenv import load_dotenv
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Muat environment variables dari file .env (hanya untuk development lokal)
load_dotenv(os.path.join(BASE_DIR, '.env'))

# ==============================================================================
# PENGATURAN KUNCI & KEAMANAN UNTUK PRODUKSI
# ==============================================================================

# SECRET_KEY diambil dari environment variable. JANGAN DITARUH DI SINI.
SECRET_KEY = os.environ.get('SECRET_KEY')

# DEBUG=False di produksi untuk keamanan. 
# Nilainya diambil dari environment variable, defaultnya False.
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

# ALLOWED_HOSTS akan diisi otomatis oleh Render.
# Untuk lokal, Anda bisa menambahkan '127.0.0.1' jika perlu.
ALLOWED_HOSTS = []
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# ==============================================================================
# APLIKASI & MIDDLEWARE
# ==============================================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage', # Taruh sebelum staticfiles untuk manajemen file
    'django.contrib.staticfiles',
    'cloudinary', # Taruh setelah staticfiles
    'kuliner',
    'crispy_forms',
    "crispy_bootstrap5",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Middleware untuk WhiteNoise (file statis)
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ==============================================================================
# KONFIGURASI INTI DJANGO
# ==============================================================================

# Pastikan nama proyek Anda adalah 'petarasa_project'. Jika berbeda, sesuaikan.
ROOT_URLCONF = 'petarasa_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Tambahkan ini jika Anda punya template global
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'petarasa_project.wsgi.application'


# ==============================================================================
# DATABASE (Bisa untuk Lokal & Produksi)
# ==============================================================================

# Menggunakan dj_database_url untuk membaca konfigurasi database dari environment variable.
# Jika tidak ada DATABASE_URL, akan menggunakan SQLite sebagai default untuk lokal.
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600
    )
}


# ==============================================================================
# VALIDASI PASSWORD & INTERNASIONALISASI
# ==============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'id'
TIME_ZONE = 'Asia/Jakarta'
USE_I18N = True
USE_TZ = True


# ==============================================================================
# FILE STATIS & MEDIA (Untuk Produksi & Lokal)
# ==============================================================================

# --- Konfigurasi File Statis (CSS, JS) untuk Produksi ---
STATIC_URL = '/static/'
# Direktori tempat `collectstatic` akan mengumpulkan semua file statis.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Menggunakan WhiteNoise untuk menyimpan file statis yang terkompresi.
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DIRS = [
    BASE_DIR / 'kuliner/static',
]

# --- Konfigurasi File Media (Upload Pengguna) menggunakan Cloudinary ---
# MEDIA_URL dan MEDIA_ROOT tidak diperlukan saat menggunakan Cloudinary.
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
CLOUDINARY_URL = os.environ.get('CLOUDINARY_URL')


# ==============================================================================
# PENGATURAN LAINNYA
# ==============================================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"