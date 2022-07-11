from asyncio.windows_events import NULL
from atexit import register
from gettext import NullTranslations
import json
from pickle import EMPTY_SET
from .models import *
from django.http import BadHeaderError
from django.shortcuts import redirect, render
from urllib import request
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate ,login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail,BadHeaderError
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

#======= loading Sections=====

# admin page

def load_admin_dashbord_login(request):
    return render(request,'AdminLogin.html')

def load_AdminDashboard(request):
    folders=galleryfolder.objects.all()
    return render(request,'DashBoard.html',{'folders':folders})

def admin_gallery_add(request):
    images=gallery.objects.all()
    return render(request,'admin_gallery.html',{'images':images})

def admin_affiliation_load(request):
    affili=affiliation.objects.get(id=1)
    return render(request,'admin_affiliation.html',{'affili':affili})

@csrf_exempt
def admin_affiliation_add(request):
    if request.method=="POST":
        fileimg=request.FILES.get('affi_cover')
        file=request.FILES.get('affi_pdf')
        aff=affiliation.objects.all()
        print(aff)
        if (aff==0):
            affiliation.objects.create(affi_name=file,affi_img=fileimg)
        else:
            affi=affiliation.objects.get(id=1)
            affi.affi_img=fileimg
            affi.affi_name=file
            affi.save() 
        return redirect('admin_affiliation_load')

def admin_event_gallery(request,admin_folder_id):
    folder=galleryfolder.objects.get(id=admin_folder_id)
    images=gallery.objects.filter(folder_id=admin_folder_id)
    return render(request,'admin_event_gallery.html',{'folder':folder,'images':images})

def Assmember_Register(request):
    return render(request,'AssociateMemberRegister.html')

@csrf_exempt
def associate_members_add(request):
    if request.method=="POST":
        assname=request.POST['ass_name']
        phno=request.POST['ass_no']
        mailid=request.POST['ass_email']
        position=request.POST['ass_position']
        img=request.FILES.get('imgs')

    #saving data
        associate_members.objects.create(asm_name=assname,asm_phno=phno,asm_email=mailid,asm_position=position,asm_image=img,)

        return redirect('load_AdminDashboard')

# admin folder create
 
def create_folder(request):
    if request.method=="POST":
        fname=request.POST['filename']
        image=request.FILES.get('cover_imgs')

 #saving data

        folder=galleryfolder(folder_name=fname,folder_image_url=image)

        folder.save()
        return redirect('load_AdminDashboard')
    else:
        return redirect('load_AdminDashboard')

#adding images to a folder 
@csrf_exempt
def add_images_gallery(request):
    if request.method=='POST':
        name=request.POST['filename']
        print(name)
        image=request.FILES.getlist('imgsfile')
        folderid=galleryfolder.objects.get(folder_name=name)
        for imag in image:
            gallery.objects.create(
                image_url=imag,
                folder_id=folderid)
        return redirect('admin_event_gallery',folderid.id)


# index page
def load(request):
    return render(request,'Lenage.html')
def index_load(request):
    folders=galleryfolder.objects.all()
    return render(request,'index.html',{'folders':folders})

def load_member(request):
    return render(request,'assmembers.html')

def load_affiliation(request):
    affili=affiliation.objects.get(id=1)
    return render(request, 'affiliation.html',{'affili':affili})

def load_kata(request):
    return render(request,'kata.html')

def MoreEvent(request,galley_id):
    folders=galleryfolder.objects.all()
    images=gallery.objects.filter(folder_id=galley_id)
    return render(request,'MoreEvents.html',{'folders':folders,'images':images})

def MoreEventall(request):
    folders=galleryfolder.objects.all()
    images=gallery.objects.all()
    return render(request,'MoreEvents.html',{'folders':folders,'images':images})

def preload(request):
    return render(request,'preload.html')