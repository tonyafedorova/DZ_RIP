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
from dzrip.views import first, pictures, forLab5, Profile, firstnotlog, picturenotlog, signup, MyLoginView, logout, profedit, changepass

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', first, name='root'),
    url(r'^pictures/', pictures),
    path('lab5/', forLab5.as_view()),
    path('profile/', Profile),
    path('firstnotlog/', firstnotlog, name='firstnotlog'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('picnotlog/', picturenotlog),
    path('signup/', signup, name='signup'),
    path('logout/', logout),
    path('profile/edit/', profedit, name='edit'),
    path('profile/password/', changepass, name='change')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
