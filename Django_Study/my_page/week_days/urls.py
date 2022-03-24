from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_info_by_kianu),
    path('<int:day>/', views.get_info_by_number),
    path('<str:day>/', views.get_info, name='todo_week_str')
]
