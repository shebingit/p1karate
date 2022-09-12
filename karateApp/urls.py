from django.views import *
from django.urls import  path,reverse_lazy
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
                path('changepassword',views.changepassword,name='changepassword'),

                #admin load sections

                path('Assmember_Register',views.Assmember_Register,name='Assmember_Register'),
                path('admin_gallery_add',views.admin_gallery_add,name='admin_gallery_add'),
                path('admin_event_gallery/<int:admin_folder_id>',views.admin_event_gallery,name='admin_event_gallery'),
                path('create_folder',views.create_folder,name='create_folder'),
                path('content_load',views.content_load,name='content_load'),
                path('create_content',views.create_content,name='create_content'),
                path('graduation_add',views.graduation_add,name='graduation_add'),
                path('graduvationuploadedit/<int:grdu_id>',views.graduvationuploadedit,name='graduvationuploadedit'), 
                path('graduation_update/<int:grudup_id>',views.graduation_update,name='graduation_update'), 
                path('graduvationdelete/<int:grduddelete_id>',views.graduvationdelete,name='graduvationdelete'),
                path('loadcontupdate/<int:contupdateload>',views.loadcontupdate,name='loadcontupdate'),
                path('update_content/<int:contsave>',views.update_content,name='update_content'),
                path('loadsubcontent/<int:subcontid>',views.loadsubcontent,name='loadsubcontent'),
                path('subcreate_content/<int:subcontentadd_id>',views.subcreate_content,name='subcreate_content'),
                path('subcontentupload/<int:subcontupid>',views.subcontentupload,name='subcontentupload'),
                path('update_sbcontent/<int:subcontaddid>',views.update_sbcontent,name='update_sbcontent'),
                path('subcontent_delete/<int:subcont_deleteid>',views.subcontent_delete,name='subcontent_delete'),
                path('add_images_gallery',views.add_images_gallery,name='add_images_gallery'),
                path('associate_members_add',views.associate_members_add,name='associate_members_add'),
                path('admin_affiliation_load',views.admin_affiliation_load,name='admin_affiliation_load'),
                path('admin_affiliation_add',views.admin_affiliation_add,name='admin_affiliation_add'),
                path('load_folder_update/<int:fupid>',views.load_folder_update,name='load_folder_update'),
                path('updatename_folder/<int:folder_upid>',views.updatename_folder,name='updatename_folder'),
                path('load_admin_katas',views.load_admin_katas,name='load_admin_katas'),
                path('admin_event/<int:admin_event_id>',views.admin_event,name='admin_event'),
                path('news_images/<int:eventimg_id>',views.news_images,name='news_images'),
                path('event_img_delet/<int:evemt_img_delete>',views.event_img_delet,name='event_img_delet'),
                path('regform_upload/<int:from_id>',views.regform_upload,name='regform_upload'),

                # admin delete sections
                
                path('admin_member_delete/<int:ad_member_id>',views.admin_member_delete,name='admin_member_delete'),
                path('admin_folder_delete/<int:ad_delete_id>',views.admin_folder_delete,name='admin_folder_delete'),
                path('admin_gallery_delete/<int:ad_gallery_id>',views.admin_gallery_delete,name='admin_gallery_delete'),
                path('uplod_link',views.uplod_link,name='uplod_link'),
                path('news_upload',views.news_upload,name='news_upload'), 
                path('news_delete/<int:news_id>',views.news_delete,name='news_delete'),
                path('eventform_delete/<int:eventform_id>',views.eventform_delete,name='eventform_delete'),
                path('admincontent_delete/<int:adcont_deleteid>',views.admincontent_delete,name='admincontent_delete'),




                #user page load 
                #path('preload',views.preload,name='preload'),
                path('',views.index_load,name='index_load'),
                path('About_karate',views.About_karate,name='About_karate'),
                path('load_jain',views.load_jain,name='load_jain'),
                path('load_JainMelord/<int:loadcontid>',views.load_JainMelord,name='load_JainMelord'),
                path('load_member',views.load_member,name='load_member'),
                path('load_affiliation',views.load_affiliation,name='load_affiliation'),
                path('load_kata',views.load_kata,name='load_kata'),
                path('history',views.history,name='history'),

                # HISTORY SINGLE PAGE
                
                
                path('history1',views.history1,name='history1'),
                path('history2',views.history2,name='history2'),
                path('history3',views.history3,name='history3'),
                path('history4',views.history4,name='history4'),
                path('load_jainsmaster',views.load_jainsmaster,name='load_jainsmaster'),

                

                path('MoreEvent/<int:galley_id>',views.MoreEvent,name='MoreEvent'),
                path('MoreEventall',views.MoreEventall,name='MoreEventall'),
                path('load_events/<int:event_id>',views.load_events,name='load_events'),
                path('send_message',views.send_message,name='send_message'),
                path('usermsgdelete/<int:msgdelete_id>',views.usermsgdelete,name='usermsgdelete'),
                path('eventcontentdelete/<int:eventcontdeleteid>',views.eventcontentdelete,name='eventcontentdelete'), 
                path('load_aboutkarate',views.load_aboutkarate,name='load_aboutkarate'), 
                


                #password reset

                path('load_passwordchange',views.load_passwordchange,name='load_passwordchange'),
                 
               path('password_change/', auth_views.PasswordChangeView.as_view(template_name='account_password.html',success_url=reverse_lazy('password_change_done')), 
                name='password_change'),

               path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), 
                name='password_change_done'),

                

                 # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
          #   path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
          #   name='password_change_done'),

          #   path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
          #   name='password_change'),

          #   path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
          #   name='password_reset_done'),

          #   path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
          #   path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
          #   path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
          #   name='password_reset_complete'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)