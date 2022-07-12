from django.views import *
from django.urls import  path
from django.conf import settings
from django.conf.urls.static import static
from .import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

                 #admin  page load login sections

urlpatterns =[  path('Admin11212Dashbord_Login',views.Admin11212Dashbord_Login,name='Admin11212Dashbord_Login'),
                path('adminlogin',views.adminlogin,name='adminlogin'),
                path('load_AdminDashboard',views.load_AdminDashboard,name='load_AdminDashboard'),
                path('logout',views.logout,name='logout'),

                #admin load sections

                path('Assmember_Register',views.Assmember_Register,name='Assmember_Register'),
                path('admin_gallery_add',views.admin_gallery_add,name='admin_gallery_add'),
                path('admin_event_gallery/<int:admin_folder_id>',views.admin_event_gallery,name='admin_event_gallery'),
                path('create_folder',views.create_folder,name='create_folder'),
                path('add_images_gallery',views.add_images_gallery,name='add_images_gallery'),
                path('associate_members_add',views.associate_members_add,name='associate_members_add'),
                path('admin_affiliation_load',views.admin_affiliation_load,name='admin_affiliation_load'),
                path('admin_affiliation_add',views.admin_affiliation_add,name='admin_affiliation_add'),

                # admin delete sections

                path('admin_folder_delete/<int:ad_delete_id>',views.admin_folder_delete,name='admin_folder_delete'),
                path('admin_gallery_delete/<int:ad_gallery_id>',views.admin_gallery_delete,name='admin_gallery_delete'),




                #user page load 
    
                path('',views.index_load,name='index_load'),
                path('load_member',views.load_member,name='load_member'),
                path('load_affiliation',views.load_affiliation,name='load_affiliation'),
                path('load_kata',views.load_kata,name='load_kata'),
                path('history',views.history,name='history'),
                path('preload',views.preload,name='preload'),
                path('MoreEvent/<int:galley_id>',views.MoreEvent,name='MoreEvent'),
                path('MoreEventall',views.MoreEventall,name='MoreEventall'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)