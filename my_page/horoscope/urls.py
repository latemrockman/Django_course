from django.urls import path
from . import views

urlpatterns = [
    path('16/', views.get_info_about_16),
    path('<int:sign_zodiak>/', views.get_info_about_sign_zodiak_by_number),
    path('<str:sign_zodiak>/', views.get_info_about_sign_zodiak_by_string),
]