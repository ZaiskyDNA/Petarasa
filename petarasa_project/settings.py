import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================================================================
# PENGATURAN KUNCI & KEAMANAN
# ==============================================================================

# PENTING: Ganti dengan secret key yang kuat dan acak untuk produksi!
# Anda bisa membuatnya di https://djecrety.ir/
SECRET_KEY = 'ganti-dengan-secret-key-anda-yang-sebenarnya'

# Matikan DEBUG di produksi untuk keamanan.
DEBUG = False

# Sesuaikan dengan username PythonAnywhere Anda.
ALLOWED_HOSTS = ['petarasa.pythonanywhere.com', '127.0.0.1']


# ==============================================================================
# APLIKASI & MIDDLEWARE
# ==============================================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage', # Untuk manajemen file media
    'django.contrib.staticfiles',
    'cloudinary',
    'kuliner',
    'crispy_forms',
    "crispy_bootstrap5",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # WhiteNoise tidak diperlukan di PythonAnywhere
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

# Ganti 'petarasa_project' jika nama folder proyek Anda berbeda.
ROOT_URLCONF = 'petarasa_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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
# DATABASE (Untuk PythonAnywhere)
# ==============================================================================

# Isi detail ini dari tab "Databases" di dashboard PythonAnywhere Anda.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nama-user-anda$default',
        'USER': 'nama-user-anda',
        'PASSWORD': 'password-mysql-anda',
        'HOST': 'nama-user-anda.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
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
# FILE STATIS & MEDIA
# ==============================================================================

# --- Konfigurasi File Statis (CSS, JS) untuk PythonAnywhere ---
STATIC_URL = '/static/'
# Direktori tempat `collectstatic` akan mengumpulkan semua file statis.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# --- Konfigurasi File Media (Upload Pengguna) menggunakan Cloudinary ---
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
# Anda perlu mengatur CLOUDINARY_URL sebagai environment variable di PythonAnywhere
# atau menuliskannya langsung di sini jika tidak terlalu rahasia.
# Contoh: CLOUDINARY_URL = 'cloudinary://key:secret@cloudname'
CLOUDINARY_URL = os.environ.get('CLOUDINARY_URL')


# ==============================================================================
# PENGATURAN LAINNYA
# ==============================================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
