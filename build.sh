#!/bin/bash

# 1. Install semua library dari requirements.txt menggunakan pip3
pip3 install -r requirements.txt

# 2. Kumpulkan file statis
python3 manage.py collectstatic --noinput

# 3. Jalankan migrasi database
python3 manage.py migrate
