"""
в командной строке:
django-admin			                # вывести список команд
django-admin startproject first         # создать проект first
"""

############################################################################################################
создание проекта

1. django-admin startproject first      # создать проект first
2. python manage.py runserver           # запуск локального веб сервера

127.0.0.1 - локальный сервера

http://127.0.0.1:8000/          # локальный сервер
http://localhost:8000/          # то же самое

список всех "приложений" в файле settings.py  в списке INSTALLED_APPS

3. python manage.py startapp video      # создать приложение video (аналог модуля)
4. подключить приложение - в файле settings.py  в список INSTALLED_APPS добавить элемент "video"

############################################################################################################
URLs and Views


1. django-admin startproject my_page            # создали проект my_page
2  python manage.py startapp horoscope          # создали приложение horoscope
3. python manage.py startapp horoscope          # запускае сервер

URL - унифицированный указатель ресурса
Views - представление. код, который выполняется для разных URLs (функция или класс)

на каждый url должен быть свое представление

4. в папке my_page в файле urls.py добавить path('horoscope/leo', leo),
'horoscope/leo' - url
leo - функция в папке horoscope/views.py

функции во views обязательно должны принимать аргумент (принято request)

from horoscope.views import leo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('horoscope/leo', leo),                 
]

5. добавить в файл views.py 
from django.http import HttpResponse

def leo(request):
    return HttpResponse("знак зодиака Лев")



############################################################################################################
создание URLs config


1. в папке horoscope создать файл urls.py:

from django.urls import path
from . import views

urlpatterns = [
    path('leo', views.leo),
    path('scorpio', views.scorpio),
]

2. в файле my_page/urls.py изменить urlpatterns:

urlpatterns = [
    path('admin/', admin.site.urls),
    path('horoscope/', include("horoscope.urls")),
]


############################################################################################################
отладка Django in PyCharm

1. нажать кнопку Add Configuration
    -нажать +,
    - выбрать Python,
    - название Zodiak,
    - рабочая дирктория my_page (наш проект)
    - после этого должна подставиться версия Питона
    - Parametrs: manage.py runserver
 


############################################################################################################
Динамический URL

1. в файле views.py создать функцию:

def get_info_about_sign_zodiak(request, sign_zodiak):
    dict_zodiak = {
        "aries"         : "Овен     - 21 марта — 20 апреля",
        "taurus"        : "Телец    - 21 апреля — 20 мая",
        "gemini"        : "Близнецы - 21 мая — 21 июня",
        "cancer"        : "Рак      - 22 июня — 22 июля",
        "leo"           : "Лев      - 23 июля — 23 августа",
        "virgo"         : "Дева     - 24 августа — 23 сентября",
        "libra"         : "Весы     - 24 сентября — 23 октября",
        "scorpio"       : "Скорпион - 24 октября — 22 ноября",
        "sagittarius"   : "Стрелец  - 23 ноября — 21 декабря",
        "capricorn"     : "Козерог  - 22 декабря — 20 января",
        "aquarius"      : "Водолей  - 21 января — 20 февраля",
        "pisces"        : "Рыбы     - 21 февраля — 20 марта",
    }

    if sign_zodiak in dict_zodiak:
        return HttpResponse(dict_zodiak[sign_zodiak])
    else:
        return HttpResponseNotFound(f"{sign_zodiak} - неизвестный знак зодиака")

2. в файле horoscope/urls.py

urlpatterns = [
    path('<sign_zodiak>', views.get_info_about_sign_zodiak),
    #path('leo', views.leo),
    #path('scorpio', views.scorpio),
]

3. в файле my_page/urls.py

удалить - from horoscope.views import leo

############################################################################################################
Конверторы роутов

1. в файле views меняем функцию, словарь переносим в глобальную область

def get_info_about_sign_zodiak(request, sign_zodiak):
    description = dict_zodiak.get(sign_zodiak, None)

    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f"{sign_zodiak} - неизвестный знак зодиака")
        
        
##  при запросах несуществующего ключа - статус ответа 404 ()
    при запросах существующего ключа - статус ответа 200
    
    этот статус выставляет сам класс HttpResponse (200) и HttpResponseNotFound (404)


2. в файле urls:

urlpatterns = [
    path('16/', views.get_info_about_16),                                       # если ввели 16
    path('<int:sign_zodiak>/', views.get_info_about_sign_zodiak_by_number),     # если ввели число
    path('<str:sign_zodiak>/', views.get_info_about_sign_zodiak_by_string),     # если ввели строку
]

    преобразование роутов идет сверху вниз (перебор списка), тут сначала пробует преобразовать в число, 
    если это возможно то преобразует, если нет то следующий элемент списка (в строку)
    
3. views:

def get_info_about_sign_zodiak_by_number(request, sign_zodiak: int):
    return HttpResponse(f'это число {sign_zodiak}')


def get_info_about_sign_zodiak_by_string(request, sign_zodiak: str):
    description = dict_zodiak.get(sign_zodiak, None)

    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f"{sign_zodiak} - неизвестный знак зодиака")
        
def get_info_about_16(request):
    return HttpResponse(f'This is 16')
    
    

############################################################################################################
15 Redirect Url в Django. Перенаправление адреса в Django 3

начиная с Python версии 3.7 гарантируется, что пары словаря располагаются в том порядке, в котором они добавлялись

views:
def get_info_about_sign_zodiak_by_number(request, sign_zodiak: int):
    zodiacs = list(dict_zodiak)
    if sign_zodiak > len(zodiacs):
        return HttpResponseNotFound(f"Был передан неправильный порядковый номер - {sign_zodiak}")
    else:
        name_zodiac = zodiacs[sign_zodiak - 1]
        return HttpResponseRedirect(f"/horoscope/{name_zodiac}")


def get_info_about_111(request):
    return HttpResponseRedirect(f'https://mail.ru/')


def get_info_about_555(request):
    return HttpResponse(f'This is 555')        
        
№
urls:
urlpatterns = [
    path('111/', views.get_info_about_111),
    path('555/', views.get_info_about_555),
    path('<int:sign_zodiak>/', views.get_info_about_sign_zodiak_by_number),
    path('<str:sign_zodiak>/', views.get_info_about_sign_zodiak_by_string),
]


############################################################################################################
16 Функция reverse

Каждому нашему urlu дать определенное имя (зарегистрировать за ним определенное название и уже ссылаться потом на это название)

urls.py:

1.
это:
urlpatterns = [
    path('111/', views.get_info_about_111),
    path('555/', views.get_info_about_555),
    path('<int:sign_zodiak>/', views.get_info_about_sign_zodiak_by_number),
    path('<str:sign_zodiak>/', views.get_info_about_sign_zodiak_by_string),
]

заменить на это:
# добавляем аргемент name - это имя за которым будет зарегистрирован url
urlpatterns = [
    path('111/', views.get_info_about_111, name = "horoscope-name"),
    path('555/', views.get_info_about_555, name = "horoscope-name"),
    path('<int:sign_zodiak>/', views.get_info_about_sign_zodiak_by_number, name = "horoscope-name"),
    path('<str:sign_zodiak>/', views.get_info_about_sign_zodiak_by_string, name = "horoscope-name"),
]

2. импортируем в файл views функцию reverse

from django.urls import reverse

reverse("horoscope-name", args = (nam e_zodiak))

# функция reverse() пытается воссоздать url по имени "horoscope-name". 
# т.е. она отыскивает где используется path (он используется в horoscope/urls.py в списке urlpatterns)
# а в этот path мы попадем только когда сработает в файле my_page/urls.py:
urlpatterns = [
    path('admin/', admin.site.urls),
    path('horoscope/', include("horoscope.urls")),
]

def get_info_about_sign_zodiak_by_number(request, sign_zodiak: int):
    zodiacs = list(dict_zodiak)
    if sign_zodiak > len(zodiacs):
        return HttpResponseNotFound(f"Был передан неправильный порядковый номер - {sign_zodiak}")

    name_zodiac = zodiacs[sign_zodiak - 1]
    redirect_url = reverse("horoscope-name", args=(name_zodiac))
    return HttpResponseRedirect(redirect_url)
#
############################################################################################################
16 Функция reverse

1. в функции def get_info_about_sign_zodiak_by_string(request, sign_zodiak: str) изменяем строку:

return HttpResponse(f"<h2>{description}</h2>")

2. в файле horoscope/urls добавляем путь с пустой строчкой

    path('', views.index),
#
3. views:

def index(request):
    zodiacs = list(dict_zodiak)

    li_elements = ""

    for sign in zodiacs:
        redirect_path = reverse("horoscope-name", args=[sign])
        li_elements += f"<li><a href ='{redirect_path}'>{sign.title()}</a></li>"
    response = f"""
    <ul>
        {li_elements}
    </ul>
"""
    return HttpResponse(response)
    
    
############################################################################################################
#18-1 Создаем собственный конвертер 

from django.urls import path, converters  - converters модуль, тут можно посмотреть встроенные конвертеры


class StringConverter:                  # конвертер должен представлять собой класс (имя выбираем сами). в классе должны быть три составляющие:
    regex = "[^/]+"                     # 1. регулярное выражение (переменная regex) по нему будет искаться строка в роуте

    def to_python(self, value):         # 2. если значение нашлось, то строка будет поступать на функцию to_python
        return value                    # в этой функц нужно преобразовать строку в нужный мне объект

    def to_url(self, value):            # 3. обратное преобразование - из объекта, преобразует представление строки
        return value
#

1. создаем файл converters.py в папке с проектом (там же где и views.py), туда пишем класс конвертера:
class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value

2. регистрируем - в url конфиге (файл urls.py):
from django.urls import path, register_converter    # добавили register_converter
from . import views, converters                     # файл converters


3. регистрируем, добавляем строчку:
register_converter(converters.FourDigitYearConverter, 'yyyy')

4. в urlpatterns добавляем:
    path('<yyyy:sign_zodiac>/', views.get_yyyy_converters),
№

5. в файле views добавляем соответствующую функцию:
def get_yyyy_converters(request, sign_zodiac):
    return HttpResponse(f"Вы передали число из четырёх чисел - {sign_zodiac}")
№

Делаем еще один конвертер:

1. добавляем класс в converters.py
class MyFloatConverter:
    regex = '[+-]?(\d*\.)?\d+'

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value)
#
2. регистрируем конвертер:
- добавляем строчку register_converter(converters.MyFloatConverter, 'my_float')
- в urlpatterns добавляем:      path('<my_float:sign_zodiac>/', views.get_my_float_converters),

3. views добавляем:
def get_my_float_converters(request, sign_zodiac):
    return HttpResponse(f"Вы передали вещественное число - {sign_zodiac}")
    
# Еще один конвертер (MyDateConverter):

class MyDateConverter:
    regex = '^(0[1-9]|[12][0-9]|3[01])[-](0[1-9]|1[012])[-](19|20)\d\d$'

    def to_python(self, value):
        return datetime.strptime(value, '%d-%m-%Y')

    def to_url(self, value):
        return value.strftime('%d-%m-%Y')
#
register_converter(converters.MyDateConverter, 'my_date')

urlpatterns - path('<my_date:sign_zodiac>', views.get_my_date_converters),

############################################################################################################
# 19 шаблоны в django

1. создаем папку templates в horoscope (общепринятое место)
2. внутри templates создаем еще одну папку с названием нашего приложения "horoscope"
3. в новой папке horoscope создаем info_zodial.html и редактируем его
4. в файле views импортируем from django.template.loader import render_to_string
5. views изменяем функцию:
def get_info_about_sign_zodiak_by_string(request, sign_zodiak: str):
    response = render_to_string('horoscope/info_zodiac.html')
    return HttpResponse(response)
6. settings.py:
TEMPLATES -> DIRS - в этом списке указываются абсолютные пути к шаблонам
BASE_DIR - это абсолютный путь к проекту, 

TEMPLATES -> DIRS -> 'DIRS': [BASE_DIR / "horoscope" / "templates"]   - это менее предпочтительный способ

#'APP_DIRS': True, -тру значит, что джанго автоматически в каждом приложении проекта будет искать папку templates

ПРЕДПОЧТИТЕЛЬНЫЙ ВАРИАНТ:
1. settings.py -> INSTALLED_APPS -> добавить 'horoscope' (название лежит в файле apps.py)


############################################################################################################
# 20 поиск шаблонов


render() заменяет render_to_string('horoscope/info_zodiac.html') и HttpResponse():

изначально:
def get_info_about_sign_zodiak_by_string(request, sign_zodiak: str):
    response = render_to_string('horoscope/info_zodiac.html')
    return HttpResponse(response)

можно заменить на:

from django.shortcuts import render

def get_info_about_sign_zodiak_by_string(request, sign_zodiak: str):
    return render(request, 'horoscope/info_zodiac.html')