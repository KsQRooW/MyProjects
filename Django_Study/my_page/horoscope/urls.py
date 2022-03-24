from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('type/', views.types, name='horoscope_type'),
    path('type/<str:element_type>/', views.get_info_by_type, name='horoscope_type'),
    path('<int:sign_zodiac>/', views.get_info_by_number),
    path('<str:sign_zodiac>/', views.get_info, name='horoscope-name'),
    path('<int:month>/<int:day>/', views.get_info_by_date)
]
