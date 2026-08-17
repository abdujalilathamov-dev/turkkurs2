#!/usr/bin/env python
"""Django loyihasini boshqarish uchun buyruqlar interfeysi."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'turkkurs.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django o'rnatilmagan yoki topilmadi. 'python -m pip install -r requirements.txt' "
            "buyrug'ini bajaring."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
