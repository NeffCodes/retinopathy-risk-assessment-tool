"""
URL configuration for rrat project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),  # Homepage
    path('about/', views.about, name='about'),  # About Page
    path('patients/', include(('patients.urls', 'patients'), namespace='patients')),
    path('retina_photos/', include(('retina_photos.urls', 'retina_photos'), namespace='retina_photos')),
    path('users/', include('users.urls')),
]