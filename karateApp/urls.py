from django.views import *
from django.urls import  path
from django.conf import settings
from django.conf.urls.static import static
from .import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns =[  path('',views.index_load,name='index_load'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)