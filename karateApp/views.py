from atexit import register
import json
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

def load_AdminDashboard(request):
    return render(request,'DashBoard.html')

# index page

def index_load(request):
    return render(request,'index.html')

def load_member(request):
    return render(request,'assmembers.html')

def load_affiliation(request):
    return render(request, 'affiliation.html')

def load_kata(request):
    return render(request,'kata.html')

def MoreEvent(request):
    return render(request,'MoreEvents.html')

def preload(request):
    return render(request,'preload.html')