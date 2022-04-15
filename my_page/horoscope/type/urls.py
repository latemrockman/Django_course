from django.urls import path
from horoscope import views

urlpatterns = [
    path('', views.type_index),
    #path('fire/', views.get_fire, name = "horoscope-name"),
    path('<str:sign_type>/', views.get_zodiac_type, name="type-name"),
]