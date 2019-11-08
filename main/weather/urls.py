from django.contrib import admin
from django.urls import path
from .views import WeatherView, DeleteView
from . import views

urlpatterns = [
    path('weather/', views.WeatherView),
    path('delete/<city_name>/', DeleteView.as_view()),
]
