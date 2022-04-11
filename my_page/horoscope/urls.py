from django.urls import path
from . import views

urlpatterns = [
    path('111/', views.get_info_about_111),
    path('555/', views.get_info_about_555),
    path('<int:sign_zodiak>/', views.get_info_about_sign_zodiak_by_number),
    path('<str:sign_zodiak>/', views.get_info_about_sign_zodiak_by_string),
]