from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MyFloatConverter, 'my_float')
register_converter(converters.MyDateConverter, 'my_date')


urlpatterns = [
    path('', views.index, name = "horoscope-index"),
    path('<my_date:sign_zodiac>', views.get_my_date_converters),
    path('<yyyy:sign_zodiac>/', views.get_yyyy_converters),
    path('<int:month>/<int:day>/', views.get_info_by_date),
    path('111/', views.get_info_about_111, name = "horoscope-name"),
    path('555/', views.get_info_about_555, name = "horoscope-name"),
    path('<int:sign_zodiak>/', views.get_info_about_sign_zodiak_by_number, name = "horoscope-name"),
    path('<my_float:sign_zodiac>/', views.get_my_float_converters),
    path('<str:sign_zodiak>/', views.get_info_about_sign_zodiak_by_string, name = "horoscope-name"),
]