#!/usr/bin/env python
# resim işlemleri için Pillow adlı Python kütüphanesini kurmamız gerekmektedir.  pip install Pillow komut satırı ile
#dosya yükleme işlemleri için gerekli kodlar yazıldıktan sonra bu değişiklikleri veri tabanına bildirmek gerekiyor
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_Tekrar.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
