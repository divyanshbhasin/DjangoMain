from django.contrib import admin
from django.urls import path
from .views import HomeView, LogoutView, NotLoggedView, NoFormView, NewVideo, VideoFileView, VideoView, CommentView

urlpatterns = [
    path('video/', HomeView.as_view()),
    path('new_video/', NewVideo.as_view()),
    path('notlogged/', NotLoggedView.as_view()),
    path('noform/', NoFormView.as_view()),
    path('video/<int:id>/', VideoView.as_view()),
    path('comment', CommentView.as_view()),
    path('get_video/<file_name>/', VideoFileView.as_view()),
    path('logout/', LogoutView.as_view()),
]
