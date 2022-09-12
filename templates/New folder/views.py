
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
from embed_video.fields import EmbedVideoField
#======= loading Sections=====

def adminlogin(request): 
    try:
        if request.method == 'POST':
            try:
                username = request.POST['uname']
                password = request.POST['psw']
                user = auth.authenticate(username=username, password=password)
                request.session["uid"] = user.id

                if user is not None:
                    auth.login(request, user)
                    if user.is_superuser==1:
                        return redirect ('load_AdminDashboard')

            except:
                messages.info(request, 'Invalid username or password')
                return render(request, 'AdminLogin.html')                        
        else:
            #messages.info(request, 'Invalid username or password')
            return render('AdminLogin.html')        
    except:
       # messages.info(request, 'Invalid username or password')
        return render(request, 'AdminLogin.html')


def logout(request):
    request.session["uid"] = ""
    auth.logout(request)
    return redirect('index_load')



# admin page

def Admin11212Dashbord_Login(request):
    return render(request,'AdminLogin.html')

@login_required
def load_AdminDashboard(request):
    news_contents=news.objects.all()
    usermsg= UserMessages.objects.all().order_by('-id')
    return render(request,'DashBoard.html',{'news_contents':news_contents,'usermsg':usermsg})

@login_required
def admin_gallery_add(request):
    folders=galleryfolder.objects.all()
    return render(request,'admin_gallery.html',{'folders':folders})

def load_folder_update(request,fupid):
    folder=galleryfolder.objects.filter(id=fupid)
    return render(request,'updatefolder.html',{'folder':folder})

def updatename_folder(request,folder_upid):
    if request.method=="POST":
        folder_update=galleryfolder.objects.get(id=folder_upid)
        folder_update.folder_name=request.POST.get('filename')
        folder_update.save()
        folders=galleryfolder.objects.all()
        return render(request,'admin_gallery.html',{'folders':folders})
    else:
        return render(request,'DashBoard.html')


@login_required
def admin_affiliation_load(request):
    affili=affiliation.objects.get(id=1)
    return render(request,'admin_affiliation.html',{'affili':affili})

@login_required
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
@login_required
def admin_event_gallery(request,admin_folder_id):
    folder=galleryfolder.objects.get(id=admin_folder_id)
    images=gallery.objects.filter(folder_id=admin_folder_id)
    return render(request,'admin_event_gallery.html',{'folder':folder,'images':images})

def Assmember_Register(request):
    members=associate_members.objects.all()
    return render(request,'AssociateMemberRegister.html',{'members':members})

@csrf_exempt
def associate_members_add(request):
    if request.method=="POST":
        assname=request.POST['ass_name']
        phno=request.POST['ass_no']
        mailid=request.POST['ass_email']
        position=request.POST['ass_position']
        con_text=request.POST['ass_text']
        img=request.FILES.get('imgs')

    #saving data
        associate_members.objects.create(asm_name=assname,asm_phno=phno,asm_email=mailid,asm_position=position,asm_image=img,asm_text=con_text)

        return redirect('load_AdminDashboard')

# admin folder create

@login_required
def create_folder(request):
    if request.method=="POST":
        fname=request.POST['filename']
        image=request.FILES.get('cover_imgs')

 #saving data

        folder=galleryfolder(folder_name=fname,folder_image_url=image)

        folder.save()
        return redirect('admin_gallery_add')
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

def load_admin_katas(request):
    vid_items=items.objects.all()
    return render(request,'admin_katas.html',{'vid_items':vid_items})


#delete sections

def admin_member_delete(request,ad_member_id):
    member_delete=associate_members.objects.get(id=ad_member_id)
    member_delete.delete()
    return redirect('Assmember_Register')

def admin_folder_delete(request,ad_delete_id):
    folder_delete=galleryfolder.objects.get(id=ad_delete_id)
    folder_delete.delete()
    return redirect('load_AdminDashboard')

def admin_gallery_delete(request,ad_gallery_id):
    gallery_delete=gallery.objects.get(id=ad_gallery_id)
    folder=galleryfolder.objects.get(id=gallery_delete.folder_id.id)
    images=gallery.objects.filter(folder_id=gallery_delete.folder_id.id)
    gallery_delete.delete()
    return render(request,'admin_event_gallery.html',{'folder':folder,'images':images})

def admin_event(request,admin_event_id):
    news_contents=news.objects.get(id=admin_event_id)
    event_gallerys=event_gallery.objects.filter(events_id=admin_event_id)
    regforms=RegisterForm.objects.filter(eventsform_id=admin_event_id)
    eventcont=Event_content.objects.filter(eventnews_id=admin_event_id)
    return render(request,'admin_event.html',{'news_contents':news_contents,'event_gallerys':event_gallerys,'regforms':regforms,'eventcont':eventcont})

def news_images(request,eventimg_id):
    if request.method=='POST':
        head=request.POST['heading']
        evcont=request.POST['content']
        eventid=news.objects.get(id=eventimg_id)
        eventscontent=Event_content(heading=head,contents=evcont,eventnews_id=eventid)
        eventscontent.save()
        image=request.FILES.getlist('news_gallery')
        if image :
            eventid=news.objects.get(id=eventimg_id)
            for imag in image:
                event_gallery.objects.create(
                    event_image_url=imag,
                    events_id=eventid)
        news_contents=news.objects.get(id=eventimg_id)
        event_gallerys=event_gallery.objects.filter(events_id=eventimg_id)
        eventcont=Event_content.objects.filter(eventnews_id=eventimg_id)
        return render(request,'admin_event.html',{'news_contents':news_contents,'event_gallerys':event_gallerys,'eventcont':eventcont})

def event_img_delet(request,evemt_img_delete):
     event_gallerys=event_gallery.objects.get(id=evemt_img_delete)
     event_gallerys.delete()
     return redirect('load_AdminDashboard')
    
def regform_upload(request,from_id):
    if request.method=="POST":
        regiform=request.FILES.get('regfom_name')
        formreg=news.objects.get(id=from_id)
        form_reg=RegisterForm(regform=regiform,eventsform_id=formreg)
        form_reg.save()
        return redirect('load_AdminDashboard')
    
def eventform_delete(request,eventform_id):
    formregdelete=RegisterForm.objects.get(id=eventform_id)
    formregdelete.delete()
    return redirect('load_AdminDashboard')




# index page

def index_load(request):
    news_contents=news.objects.all()
    disp1=Admincontent.objects.all()
    return render(request,'index.html',{'news_contents':news_contents,'disp1':disp1})

def About_karate(request):
    return render(request,'about_karate.html')

def load_member(request):
    members=associate_members.objects.all()
    return render(request,'assmembers.html',{'members':members})

def load_affiliation(request):
    affili=affiliation.objects.get(id=1)
    return render(request, 'affiliation.html',{'affili':affili})

def load_kata(request):
    k1=items.objects.get(kata_name='Geki Sai Dai Ichi')
    k2=items.objects.get(kata_name='Geki Sai Dai Ni')
    k3=items.objects.get(kata_name='Saifa')
    k4=items.objects.get(kata_name='Sanchin')
    k5=items.objects.get(kata_name='Seiyunchin')
    k6=items.objects.get(kata_name='Shisochin')
    k7=items.objects.get(kata_name='Sanseru')
    k8=items.objects.get(kata_name='Sepai')
    k9=items.objects.get(kata_name='Kururunfa')
    k10=items.objects.get(kata_name='Seisan')
    k11=items.objects.get(kata_name='Suparinpei')
    k12=items.objects.get(kata_name='Tensho')
    return render(request,'kata.html',{'k1':k1,'k2':k2,'k3':k3,'k4':k4,'k5':k5,'k6':k6,'k7':k7,'k8':k8,'k9':k9,'k10':k10,'k11':k11,'k12':k12})

def history(request):
    return render(request,'history.html')

def load_JainMelord(request,loadcontid):
    contents=Admincontent.objects.get(id=loadcontid)
    if contents.contentstatus == '1':
        no1=3
        no2=4
        
    else:
        no1=None
        no2=None
    gradu=Graduations.objects.all()
    subcont=Adminsubcontent.objects.filter(maincontid=loadcontid)
    return render(request,'jainhistory.html',{'contents':contents,'subcont':subcont,'no1':no1,'no2':no2,'gradu':gradu})



def MoreEvent(request,galley_id):
    folders=galleryfolder.objects.all()
    images=gallery.objects.filter(folder_id=galley_id)
    return render(request,'MoreEvents.html',{'folders':folders,'images':images})

def MoreEventall(request):
    folders=galleryfolder.objects.all()
    images=gallery.objects.all()
    return render(request,'MoreEvents.html',{'folders':folders,'images':images})

def preload(request):
    return render(request,'preeload.html')

def changepassword(request):
    return render(request,'registration/password_reset_form.html')

def uplod_link(request):
    if request.method=="POST":
        print(request.POST['kata'])
        print(request.POST['files'])
        vid=items.objects.get(kata_name=request.POST['kata'])
        vid.kata_name=request.POST.get('kata')
        vid.video=request.POST.get('files')
        vid.save()
        vid_items=items.objects.all()
        print(vid_items)
        messages="Video Saved Successfuly..."
        return render(request,'admin_katas.html',{'vid_items':vid_items})

def news_upload(request):
    if request.method=="POST":
        news_conts=request.POST['news_cont']
        newss=news(news_content=news_conts)
        newss.save()
        usermsg=UserMessages.objects.all()
        news_contents=news.objects.all()
        return render(request,'DashBoard.html',{'news_contents':news_contents,'usermsg':usermsg})

def news_delete(request,news_id):
    news_dele=news.objects.get(id=news_id)
    news_dele.delete()
    usermsg=UserMessages.objects.all()
    news_contents=news.objects.all()
    return render(request,'DashBoard.html',{'news_contents':news_contents,'usermsg':usermsg})

def load_events(request,event_id):
    try:
        formregform=RegisterForm.objects.get(eventsform_id=event_id)
    except RegisterForm.DoesNotExist:
        formregform=None
    eventcont=Event_content.objects.filter(eventnews_id=event_id)
    news_contents=event_gallery.objects.filter(events_id=event_id)
    return render(request,'events.html',{'news_contents':news_contents,'formregform':formregform,'eventcont':eventcont})

def send_message(request):
     if request.method=="POST":
        name=request.POST['name']
        sub=request.POST['subject']
        pho=request.POST['number']
        mail=request.POST['mail']
        msg=request.POST['message']
        usermsgs=UserMessages(uname=name,usub=sub,msgs=msg,uemail=mail,uphone=pho)
        usermsgs.save()
        message="Thank you ! We will replay soon..."
        return render(request,'index.html',{'message':message})

def usermsgdelete(request,msgdelete_id):
    msgs=UserMessages.objects.get(id=msgdelete_id)
    msgs.delete()
    news_contents=news.objects.all()
    usermsg= UserMessages.objects.all().order_by('-id')
    return render(request,'DashBoard.html',{'news_contents':news_contents,'usermsg':usermsg})

def eventcontentdelete(request,eventcontdeleteid):
    evntcont=Event_content.objects.get(id=eventcontdeleteid)
    evntcont.delete()
    news_contents=news.objects.all()
    usermsg= UserMessages.objects.all().order_by('-id')
    return render(request,'DashBoard.html',{'news_contents':news_contents,'usermsg':usermsg})


def content_load(request):
    disp=Admincontent.objects.all()
    gradu=Graduations.objects.all()
    return render(request,'content.html',{'disp':disp,'gradu':gradu})

def create_content(request):
    if request.method=="POST":
        hname=request.POST['headname']
        conts=request.POST['contents']
        img=request.FILES.get('content_img')
        contstatus=request.POST['cstatus']
        if contstatus == 1:
            content=Admincontent(headname=hname,contparagraph=conts,contimg=img,contentstatus=contstatus)
            content.save()
        else:
            counts=Admincontent.objects.filter(contentstatus=0).count()
            if counts < 1:
                content=Admincontent(headname=hname,contparagraph=conts,contimg=img,contentstatus=contstatus)
                content.save()
            else:
                messag="Sorry you can not add this Recode."
                gradu=Graduations.objects.all()
                disp=Admincontent.objects.all()
                return render(request,'content.html',{'disp':disp,'gradu':gradu,'messag':messag})


        gradu=Graduations.objects.all()
        disp=Admincontent.objects.all()
        return render(request,'content.html',{'disp':disp,'gradu':gradu})

def loadcontupdate(request,contupdateload):
    contload=Admincontent.objects.get(id=contupdateload)
    return render(request,'contentupdate.html',{'contload':contload})

def update_content(request,contsave):
    if request.method=="POST":
        contload=Admincontent.objects.get(id=contsave)
        contload.headname=request.POST.get('upheadname')
        contload.contparagraph=request.POST.get('upcontents')
        img=request.FILES.get('upcontent_img')
        contload.contentstatus=request.POST.get('upcstatus')
        if img:
            contload.contimg=img
        else:
            contload.contimg= contload.contimg

        contload.save()
        disp=Admincontent.objects.all()
        gradu=Graduations.objects.all()
        return render(request,'content.html',{'disp':disp,'gradu':gradu})

def admincontent_delete(request,adcont_deleteid):
    contdelete=Admincontent.objects.get(id=adcont_deleteid)
    contdelete.delete()
    disp=Admincontent.objects.all()
    gradu=Graduations.objects.all()
    return render(request,'content.html',{'disp':disp,'gradu':gradu})


def graduation_add(request):
     if request.method=="POST":
        gyear=request.POST['year']
        gmaster=request.POST['master']
        gkyu_year=request.POST['kyu_year']
        Graduation=Graduations(year=gyear,master=gmaster,kyuyear=gkyu_year)
        Graduation.save()
        gradu=Graduations.objects.all()
        disp=Admincontent.objects.all()
        return render(request,'content.html',{'disp':disp,'gradu':gradu})

def graduvationuploadedit(request,grdu_id):
    gradu=Graduations.objects.get(id=grdu_id)
    return render(request,'graduvationupdate.html',{'gradu':gradu})

def graduation_update(request,grudup_id):
    if request.method=="POST":
        graduation=Graduations.objects.get(id=grudup_id)
        graduation.year=request.POST.get('upyear')
        graduation.master=request.POST.get('upmaster')
        graduation.kyuyear=request.POST.get('upkyu_year')
        graduation.save()

        gradu=Graduations.objects.all()
        disp=Admincontent.objects.all()
        return render(request,'content.html',{'disp':disp,'gradu':gradu})



def graduvationdelete(request,grduddelete_id):
    gradu=Graduations.objects.get(id=grduddelete_id)
    gradu.delete()
    disp=Admincontent.objects.all()
    gradu=Graduations.objects.all()
    return render(request,'content.html',{'disp':disp,'gradu':gradu})


def loadsubcontent(request,subcontid):
    disp=Admincontent.objects.get(id=subcontid)
    subcontents=Adminsubcontent.objects.filter(maincontid=subcontid)
    return render(request,'adminsubcontent.html',{'disp':disp,'subcontents':subcontents})


def subcreate_content(request,subcontentadd_id):
     if request.method=="POST":
        disp=Admincontent.objects.get(id=subcontentadd_id)
        hname=request.POST['subheadname']
        conts=request.POST['subcontents']
       
        img=request.FILES.get('subcontent_img')
        subcontent=Adminsubcontent(subheadname=hname,subcontparagraph=conts,subcontimg=img,maincontid=disp)
        subcontents=Adminsubcontent.objects.filter(maincontid=subcontentadd_id)
        subcontent.save()
        return render(request,'adminsubcontent.html',{'disp':disp,'subcontents':subcontents})

def subcontentupload(request,subcontupid):
    subcontents=Adminsubcontent.objects.get(id=subcontupid)
    return render(request,'subcontentupdate.html',{'subcontents':subcontents})

def update_sbcontent(request,subcontaddid):
     if request.method=="POST":
        subcontent=Adminsubcontent.objects.get(id=subcontaddid)
        subcontent.subheadname=request.POST.get('upsbheadname')
        subcontent.subcontparagraph=request.POST.get('upsbcontents')
        img=request.FILES.get('upsbcontent_img')
        if img:
            subcontent.subcontimg=img
        else:
            subcontent.subcontimg= subcontent.subcontimg

        subcontent.save()
        disp=Admincontent.objects.get(id=subcontent.maincontid.id)
        subcontents=Adminsubcontent.objects.filter(maincontid=subcontent.maincontid)
        return render(request,'adminsubcontent.html',{'disp':disp,'subcontents':subcontents})


def subcontent_delete(request,subcont_deleteid):
    subcontent=Adminsubcontent.objects.get(id=subcont_deleteid)  
    mainid=subcontent.maincontid.id
    subcontent.delete()
    subcontents=Adminsubcontent.objects.filter(maincontid=mainid)
    disp=Admincontent.objects.get(id=mainid)
    return render(request,'adminsubcontent.html',{'disp':disp,'subcontents':subcontents})

def load_passwordchange(request):
    return render(request,'account_password.html')

def load_jain(request):
    contents=Admincontent.objects.get(contentstatus=1)
    if contents.contentstatus == '1':
        no1=3
        no2=4
        
    else:
        no1=None
        no2=None
    gradu=Graduations.objects.all()
    subcont=Adminsubcontent.objects.filter(maincontid=contents.id)
    return render(request,'jainhistory.html',{'contents':contents,'subcont':subcont,'no1':no1,'no2':no2,'gradu':gradu})

def load_aboutkarate(request):
    return render(request,'aboutkarate.html')


# HISTORY SINGLE PAGES

def history1(request):
    return render(request,'history1.html')

def history2(request):
    return render(request,'history2.html')

def history3(request):
    return render(request,'history3.html')

def history4(request):
    return render(request,'history4.html')

def load_jainsmaster(request):
    contents=Admincontent.objects.get(contentstatus=0)
    if contents.contentstatus == '1':
        no1=3
        no2=4
        
    else:
        no1=None
        no2=None
    gradu=Graduations.objects.all()
    subcont=Adminsubcontent.objects.filter(maincontid=contents.id)
    return render(request,'jainhistory.html',{'contents':contents,'subcont':subcont,'no1':no1,'no2':no2,'gradu':gradu})

def load_gallery(request):
    folders=galleryfolder.objects.all()
    return render(request,'gallery.html',{'folders':folders})

def load_katts(request):
    folders=galleryfolder.objects.all()
    return render(request,'allkatas.html',{'folders':folders})
