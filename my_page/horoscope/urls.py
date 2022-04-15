from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:month>/<int:day>', views.get_info_by_date),
    path('111/', views.get_info_about_111, name = "horoscope-name"),
    path('555/', views.get_info_about_555, name = "horoscope-name"),
    path('<int:sign_zodiak>/', views.get_info_about_sign_zodiak_by_number, name = "horoscope-name"),
    path('<str:sign_zodiak>/', views.get_info_about_sign_zodiak_by_string, name = "horoscope-name"),
]