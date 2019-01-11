"""DZ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import url

from DZ import settings
from dzrip.views import first, Profile, firstnotlog, signup, MyLoginView, logout, \
    profedit, changepass, PictureCreateView,  Pics, like_post

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', first, name='root'),
    path('profile/', Profile, name='profile'),
    path('firstnotlog/', firstnotlog, name='firstnotlog'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout),
    path('profile/edit/', profedit, name='edit'),
    path('profile/password/', changepass, name='change'),
    path('picture_creation/', PictureCreateView, name='picture_creation'),
    path('like/', like_post, name='like_post'),
    path('pics/', Pics.as_view(), name='pics'),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
