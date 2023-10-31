"""Diplom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Diplom import settings

urlpatterns = [
    path('main/admin/', admin.site.urls),
    path('main/', include(('persons.urls', 'persons'), namespace='persons')),
    path('main/lessons/', include(('lessons.urls', 'lessons'), namespace='lessons')),
    path('main/practice/', include(('practice.urls', 'practice'), namespace='practice')),
    path('main/lessons_practice/', include(('lessons_practice.urls', 'lessons_practice'), namespace='lessons_practice')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
