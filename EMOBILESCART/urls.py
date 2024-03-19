"""
URL configuration for DJANGOFINALPROJECT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from APP.views import HomeView

from django.conf.urls.static import static

app_name = 'APP'
app_name = 'AppleApp'
app_name = 'OneplusAPP'
app_name = 'RedmiApp'
app_name = 'SamsungApp'
app_name = 'RealmeApp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView, name='home'),
    path('APP/', include('APP.urls')),
    path('AppleApp/', include('AppleApp.urls')),
    path('OneplusApp/',include('OneplusAPP.urls')),
    path('RedmiApp/', include('RedmiApp.urls')),
    path('SamsungApp/', include('SamsungApp.urls')),
    path('RealmeApp/', include('RealmeApp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
