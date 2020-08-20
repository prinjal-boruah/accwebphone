from django.urls import path
from django.conf.urls import url,include
from . import views
from . views import *

urlpatterns = [
    path('mediacontent/', views.MediaContentListView.as_view({'get':'mediacontentList'}), name='mediacontent'),
    url(r'^videostream/(?P<did>\d+)/$',views.homeView),
    url('broadcast/',views.boradcastView,name='broadcast'),
    
    path('login',views.login_request,name='login'),
    path('',views.login_request,name='login_blank'),
    path("logout",views.logout_request,name="logout"),

    path('textcontent/',get_textContent,name='textcontent'),

    path('webphone/',webPhoneHome, name='webphone'),
    path('webphone/new/', views.post_new_webphone, name='post_new_webphone'),
    path('webphone/edit/<int:pk>/', views.webphone_edit, name='webphone_edit'),
    path('webphone/delete/<int:pk>/', views.delete_webphone, name='webphone_delete'),

    path('ipcam/',ipCamHome, name='ipcam'),
    path('ipcam/new/', views.post_new_ipcam, name='post_new_ipcam'),
    path('ipcam/edit/<int:pk>/', views.ipcam_edit, name='ipcam_edit'),
    path('ipcam/delete/<int:pk>/', views.delete_ipcam, name='ipcam_delete'),

    path('mediamaster/',mediaMasterHome, name='mediamaster'),
    path('mediamaster/new/', views.post_new_mediamaster, name='post_new_mediamaster'),
    path('mediamaster/edit/<int:pk>/', views.mediamaster_edit, name='mediamaster_edit'),
    path('mediamaster/delete/<int:pk>/', views.delete_mediamaster, name='mediamaster_delete'),
    path('mediamaster/broadcastmedia/<int:pk>/', views.broadcast_media, name='broadcast_media'),
    # path('mediamaster/broadcastmedia2/<int:pk>/<int:uid>/', views.broadcast_media, name='broadcast_media_uid'),
]