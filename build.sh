#!/bin/bash

# Membangun file statis
python3 manage.py collectstatic --noinput

# Menjalankan migrasi database
python3 manage.py migrate
