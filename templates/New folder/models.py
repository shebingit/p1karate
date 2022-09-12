from django.db import models
from tkinter import CASCADE
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField


class associate_members(models.Model):
    asm_name=models.CharField(max_length=30)
    asm_phno=models.CharField(max_length=15)
    asm_email=models.EmailField()
    asm_position=models.CharField(max_length=150)
    asm_text=models.CharField(max_length=150)
    asm_image=models.ImageField(upload_to="image/associates", null=True)

    def __str__(self):
        return self.asm_name

#image folders

class galleryfolder(models.Model):
    folder_name=models.CharField(max_length=25)
    folder_image_url=models.ImageField(upload_to="gallery/", null=True)
    
    def __str__(self):
        return self.folder_name

#images from the folder table

class gallery(models.Model):
    folder_id=models.ForeignKey(galleryfolder,on_delete=models.CASCADE,null=True,blank=True)
    image_url=models.ImageField(upload_to="gallery/", null=True)



class affiliation(models.Model):
    affi_img=models.ImageField(upload_to="file",null=True)
    affi_name=models.ImageField(upload_to="file",null=True)

class items(models.Model):
    kata_name=models.CharField(max_length=50)
    video = EmbedVideoField()  # same like models.URLField()

class news(models.Model):
    news_content=models.CharField(max_length=200)

class event_gallery(models.Model):
    events_id=models.ForeignKey(news,on_delete=models.CASCADE,null=True,blank=True)
    event_image_url=models.ImageField(upload_to="gallery/", null=True)

class RegisterForm(models.Model):
    eventsform_id=models.ForeignKey(news,on_delete=models.CASCADE,null=True,blank=True)
    regform=models.ImageField(upload_to="gallery/",null=True)

class Event_content(models.Model): 
    eventnews_id=models.ForeignKey(news,on_delete=models.CASCADE,null=True,blank=True)
    heading=models.CharField(max_length=60)  
    contents=models.TextField()

class UserMessages(models.Model):
    uname=models.CharField(max_length=25)
    usub=models.CharField(max_length=60)
    uemail=models.EmailField()
    uphone=models.CharField(max_length=60)
    msgs=models.TextField()

class Admincontent(models.Model):
    headname=models.CharField(max_length=25)
    contparagraph=models.TextField()
    contimg=models.ImageField(upload_to="gallery/",null=True)
    contentstatus=models.CharField(max_length=5)


class Adminsubcontent(models.Model):
    maincontid=models.ForeignKey(Admincontent,on_delete=models.CASCADE,null=True,blank=True)
    subheadname=models.CharField(max_length=25)
    subcontparagraph=models.TextField()
    subcontimg=models.ImageField(upload_to="gallery/",null=True)

class Graduations(models.Model):
    year=models.CharField(max_length=30)
    master=models.CharField(max_length=100)
    kyuyear=models.CharField(max_length=130)