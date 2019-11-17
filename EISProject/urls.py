"""EISProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import Posts.views
import text.views
import video.views
from django.conf import  settings
from django.conf.urls.static import static

admin.site.site_header = 'EIS  TEAM  AUTHENTICATION'                    # default: "Django Administration"
admin.site.index_title = 'UPLOAD YOUR IMAGES OR TEXT'                 # default: "Site administration"
admin.site.site_title = 'HTML title from adminsitration'

urlpatterns = [
    path('', Posts.views.homepage, name = 'homepage'),
    path('admin/', admin.site.urls),
    path('image/', Posts.views.imagepage, name = 'imagepage'),
    path('image1/', Posts.views.imagepage1, name='imagepage1'),
    path('text/',text.views.textpage, name = 'textpage' ),
    path('text1/',text.views.textpage1, name = 'textpage1' ),
    path('video/',video.views.videopage, name = 'videopage' ),
    path('video1/',video.views.videopage1, name = 'videopage1' ),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
