from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

dict_zodiak = {
    "aries": "Овен     - 21 марта — 20 апреля",
    "taurus": "Телец    - 21 апреля — 20 мая",
    "gemini": "Близнецы - 21 мая — 21 июня",
    "cancer": "Рак      - 22 июня — 22 июля",
    "leo": "Лев      - 23 июля — 23 августа",
    "virgo": "Дева     - 24 августа — 23 сентября",
    "libra": "Весы     - 24 сентября — 23 октября",
    "scorpio": "Скорпион - 24 октября — 22 ноября",
    "sagittarius": "Стрелец  - 23 ноября — 21 декабря",
    "capricorn": "Козерог  - 22 декабря — 20 января",
    "aquarius": "Водолей  - 21 января — 20 февраля",
    "pisces": "Рыбы     - 21 февраля — 20 марта",
}


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