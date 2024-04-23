
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from videos import views as video_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',include("videos.urls")),
    path('videos/',include("videos.urls")),
    path('profiles/' ,include('profiles.urls')),
    path('accounts/',include('allauth.urls')),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
