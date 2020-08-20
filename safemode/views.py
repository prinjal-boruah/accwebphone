from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.response import Response
from rest_framework.response import Response
from django.http import HttpResponse, Http404
from django.views.decorators.clickjacking import xframe_options_exempt
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework import viewsets,generics, status
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . serializers import *
from rest_framework.status import (
                                    HTTP_400_BAD_REQUEST,
                                    HTTP_404_NOT_FOUND,
                                    HTTP_200_OK
                                    )
from django.db import connection
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import datetime
import dateutil.parser
from rest_framework import generics
import django_filters.rest_framework
from django.views.generic.edit  import CreateView
from .forms import *
import requests

from postimage.views import *

datetime_obj = datetime.datetime.now()
datetime_str = datetime_obj.isoformat()
current_time = dateutil.parser.parse(datetime_str)


@xframe_options_exempt
def ok_to_load_in_a_frame(request):
    return HttpResponse("This page is safe to load in a frame on any site.") 




#_______________Media Content API_____________________________________________________________

class MediaContentListView(viewsets.ViewSet):

    def mediacontentList(self, request):
        queryset = MediaContent.objects.all()
        serializer = MediaContentSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = MediaContentSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        MediaContent = self.get_object(pk)
        MediaContent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#________________________________________________________________________________________________
@xframe_options_exempt
def homeView(request,**deviceid):
    did = deviceid['did']
    print(f"deviceid {did}")
    context = {
        "latest_media" : MediaContent.objects.filter(user_id=did).order_by('id').reverse()[0]
    }
    return render(request, 'home.html',context)

#________________________________________________________________________________________________

@xframe_options_exempt
def boradcastView(request):

    form1 = ImageForm(request.POST,request.FILES)
    print(f"request.POST : {request.POST}")
    if request.method == 'POST':
        if form1.is_valid():
            form1.save()
            return redirect('broadcast')
        else:
            return redirect('broadcast')

    context = {
        "display_loc_text" : MediaMaster.objects.filter(mediatype='text'),
        "display_loc_video" : MediaMaster.objects.filter(mediatype='video'),
        "display_loc_image" : MediaMaster.objects.filter(mediatype='image'),
        "media_data" : MediaMaster.objects.all(),
        "form1": form1,
    }
    return render(request, 'broadcast.html',context)


#_______________Login_view___________________________________________________________________
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('ipcam')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})

#_______________Logout ______________________________________________________________________
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("login")

#_______________Login Page___________________________________________________________________

def LoginView(request):
    return render(request, 'login.html')



def get_textContent(request):
    if request.method == 'POST':
        print(f"Reuest : {request.POST}")
        form = MediaTextContentForm(request.POST)
        if form.is_valid():
            print("form working")
            text_data = MediaMaster(mediatype=request.POST.get('mediatype'),mediaurl=request.POST.get('mediaurl'),isactive=1,createddate=datetime_obj)
            text_data.save()
            return redirect('broadcast')

    else:
        form = MediaTextContentForm()
    return render(request, 'broadcast.html', {'form': form})


def base_layout(request):
    return render(request, 'base.html')

@login_required
def ipCamHome(request):
    context = {
        "ipCams": Ipcams.objects.all(),
    }
    return render(request, 'ipCamHome.html',context)

@login_required
def post_new_ipcam(request):
    if request.method == "POST":     
        form = IpCamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ipcam')
    else:
        form = IpCamForm()
    return render(request, 'ipCamEdit.html', {'ip_form': form})

@login_required
def ipcam_edit(request, pk):
    ipcam = get_object_or_404(Ipcams, pk=pk)
    if request.method == "POST":
        form = IpCamForm(request.POST, instance=ipcam)
        if form.is_valid():
            form.save()
            return redirect('ipcam')
    else:
        form = IpCamForm(instance=ipcam)
    return render(request, 'ipCamEdit.html', {'ip_form': form})

def delete_ipcam(request, pk):
    ipcam = Ipcams.objects.get(pk=pk)
    ipcam.delete()
    return redirect('ipcam')

@login_required
def webPhoneHome(request):
    context = {
        "webPhones": WebphoneUsers.objects.all(),
    }
    return render(request, 'webPhoneHome.html', context)

@login_required
def post_new_webphone(request):
    if request.method == "POST":     
        form = WebPhoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('webphone')
    else:
        form = WebPhoneForm()
    return render(request, 'webPhoneEdit.html', {'webphone_form': form})

@login_required
def webphone_edit(request, pk):
    webphone = get_object_or_404(WebphoneUsers, pk=pk)
    if request.method == "POST":
        form = WebPhoneForm(request.POST, instance=webphone)
        if form.is_valid():
            form.save()
            return redirect('webphone')
    else:
        form = WebPhoneForm(instance=webphone)
    return render(request, 'webPhoneEdit.html', {'webphone_form': form})

def delete_webphone(request, pk):
    webphone = WebphoneUsers.objects.get(pk=pk)
    webphone.delete()
    return redirect('webphone')

@login_required
def mediaMasterHome(request):
    context = {
        "madiaMasters": MediaMaster.objects.all(),
        "webphone_user_names" : WebphoneUsers.objects.all(),
    }
    return render(request, 'mediaMasterHome.html',context)

@login_required
def post_new_mediamaster(request):
    if request.method == "POST":     
        form = MediaMasterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mediamaster')
    else:
        form = MediaMasterForm()
    return render(request, 'mediaMasterEdit.html', {'mm_form': form})

@login_required
def mediamaster_edit(request, pk):
    mediamaster = get_object_or_404(MediaMaster, pk=pk)
    if request.method == "POST":
        form = MediaMasterForm(request.POST, instance=mediamaster)
        if form.is_valid():
            form.save()
            return redirect('mediamaster')
    else:
        form = MediaMasterForm(instance=mediamaster)
    return render(request, 'mediaMasterEdit.html', {'mm_form': form})

def delete_mediamaster(request, pk):
    mediamaster = MediaMaster.objects.get(pk=pk)
    mediamaster.delete()
    return redirect('mediamaster')

def broadcast_media(request, pk):
    media_details = MediaMaster.objects.get(pk=pk)
    print(f"media_details : {media_details.mediatype}+++++++++++++++++++++++++")
    print(f"request.POST : {request.POST['user_id']}-----------------------")
    data = {'media_type':media_details.mediatype, 
        'url':media_details.mediaurl, 
        # 'user_id': 812, 
        'user_id': request.POST['user_id'],
        }
    r = requests.post(url = 'http://192.168.20.182:7000/mediacontent/', data = data) 
    return redirect('mediamaster')