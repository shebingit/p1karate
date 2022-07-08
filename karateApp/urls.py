from django.views import *
from django.urls import  path
from django.conf import settings
from django.conf.urls.static import static
from .import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

                 #admin  page load 

urlpatterns =[  path('load_AdminDashboard',views.load_AdminDashboard,name='load_AdminDashboard'),


                #user page load 

                path('',views.index_load,name='index_load'),
                path('load_member',views.load_member,name='load_member'),
                path('load_affiliation',views.load_affiliation,name='load_affiliation'),
                path('load_kata',views.load_kata,name='load_kata'),
                path('preload',views.preload,name='preload'),
                path('MoreEvent',views.MoreEvent,name='MoreEvent'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)