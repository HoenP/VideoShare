from . import views
from django.urls import path
from django.contrib import admin
from .views import CreateVideo,DetailVideo,UpdateVideo,DeleteVideo
from videos import views as video_views



urlpatterns = [
    #path("", views.Index, name = "home" ),
    path('', video_views.home.as_view(),name='home'),
    path("create/", CreateVideo.as_view(), name = "create-video"),
    path('<int:pk>/',DetailVideo.as_view(),name="video-detail"),
    path('<int:pk>/update',UpdateVideo.as_view(),name="video-update"),
    path('<int:pk>/delete',DeleteVideo.as_view(),name="video-delete"),
]
