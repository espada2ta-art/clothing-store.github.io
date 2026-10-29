#!/usr/bin/env python

import os
import sys


def main():
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        'clothing_store.settings'
    )

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            'Не вдалося імпортувати Django. '
            'Переконайтеся, що Django встановлений.'
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == 'main':
    main()