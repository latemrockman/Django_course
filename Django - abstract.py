"""
в командной строке:
django-admin			                # вывести список команд
django-admin startproject first         # создать проект first
"""

1. django-admin startproject first      # создать проект first
2. python manage.py runserver           # запуск локального веб сервера

127.0.0.1 - локальный сервера

http://127.0.0.1:8000/          # локальный сервер
http://localhost:8000/          # то же самое

список всех "приложений" в файле settings.py  в списке INSTALLED_APPS

3. python manage.py startapp video      # создать приложение video (аналог модуля)
4. подключить приложение - в файле settings.py  в список INSTALLED_APPS добавить элемент "video"