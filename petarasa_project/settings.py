import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# ==============================================================================
# PENGATURAN KUNCI UNTUK PRODUKSI & LOKAL
# ==============================================================================

# SECRET_KEY dibaca dari environment variable di hosting.
# Untuk lokal, gunakan kunci default jika tidak ada.
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-_x8wn627c*@!9ulq5@$)b1+ix3g6_js^9)zmkr47k!v$vzn6!j')

# DEBUG akan otomatis False di hosting, dan True di lokal (jika tidak diatur).
DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'

# ALLOWED_HOSTS untuk lokal dan hosting di Railway.
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'web-production-c2d5.up.railway.app']

# Railway akan menyediakan hostname ini secara otomatis.
RAILWAY_STATIC_HOSTNAME = os.environ.get('RAILWAY_STATIC_HOSTNAME')
if RAILWAY_STATIC_HOSTNAME:
    ALLOWED_HOSTS.append(RAILWAY_STATIC_HOSTNAME)


# ==============================================================================
# APLIKASI & MIDDLEWARE
# ==============================================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'kuliner',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # <-- Tambahkan Whitenoise di sini
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

ROOT_URLCONF = 'petarasa_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'petarasa_project.wsgi.application'


# ==============================================================================
# DATABASE
# ==============================================================================

# Konfigurasi database ini akan menggunakan PostgreSQL di Railway
# dan otomatis beralih ke SQLite di komputer lokal Anda.
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

LANGUAGE_CODE = 'id'  # Ubah ke Bahasa Indonesia
TIME_ZONE = 'Asia/Jakarta'  # Ubah ke zona waktu Indonesia
USE_I18N = True
USE_TZ = True


# ==============================================================================
# FILE STATIS & MEDIA
# ==============================================================================

# Pengaturan untuk file CSS, JavaScript, dll.
STATIC_URL = 'static/'
# Folder tempat 'collectstatic' akan mengumpulkan semua file statis untuk produksi.
STATIC_ROOT = BASE_DIR / 'staticfiles'
# Direktori tambahan tempat Django akan mencari file statis.
STATICFILES_DIRS = [BASE_DIR / 'kuliner/static']

# Penyimpanan file statis yang dioptimalkan oleh Whitenoise.
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Pengaturan untuk file yang di-upload pengguna.
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ==============================================================================
# PENGATURAN LAINNYA
# ==============================================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'