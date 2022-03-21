# import service as service
# from django.conf import settings
# from django.conf.urls.static import static

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import *



urlpatterns = [

    path('about/',about,name='about'),
    path('',index,name='home'),
    path('products/',product,name='produts'),
    path('service/',service,name='service'),
    path('new/',new,name='new'),
    path('service/', service ,name='service'),
    path('about/', about ,name='about'),
    path('dentin/<int:pk>/', product ,name='dentin'),
    # path('dentob/', product ,name='dentob'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)