from django.contrib import admin
from django.urls import path
from .views import HomeView, LoginView, RegisterView, LogoutView

urlpatterns = [
    path('', HomeView.as_view()),
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('logout/', LogoutView.as_view()),
]
