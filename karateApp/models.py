from django.db import models
from tkinter import CASCADE
from django.contrib.auth.models import User


class associate_members(models.Model):
    asm_name=models.CharField(max_length=30)
    asm_phno=models.CharField(max_length=15)
    asm_email=models.EmailField()
    asm_position=models.CharField(max_length=20)
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
