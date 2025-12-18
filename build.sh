#!/usr/bin/env bash
# Xatolik bo'lsa to'xtash
set -o errexit

# Kutubxonalarni o'rnatish
pip install -r requirements.txt

# Statik fayllarni yig'ish (Admin panel dizayni uchun)
python manage.py collectstatic --no-input

# Bazani yangilash
python manage.py migrate