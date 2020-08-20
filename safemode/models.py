
from django.db import models
from django.contrib.auth.models import AbstractUser

         

class VideoStreamStatus(models.Model):
    vss_id = models.AutoField(primary_key=True)
    vss_extn_no = models.IntegerField()
    vss_pid = models.IntegerField()
    vss_status = models.CharField(max_length=50)
    vss_stream_url = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'video_stream_status'

class MediaContent(models.Model):
    media_type = models.CharField(max_length=100, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'media_content'


class Ipcams(models.Model):
    user_id = models.AutoField(primary_key=True)
    cam_ip = models.CharField(max_length=50)
    cam_user = models.CharField(max_length=50)
    cam_pass = models.CharField(max_length=50)
    extension = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ipcams'

class LocationmediaContent(models.Model):
    locationmediaid = models.AutoField(db_column='LocationMediaID', primary_key=True,unique=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationID', blank=True, null=True)  # Field name made lowercase.
    mediatype = models.CharField(db_column='MediaType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    locationmediaurl = models.TextField(db_column='LocationMediaUrl', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LocationMedia_Content'


class LocationMaster(models.Model):
    locationid = models.AutoField(db_column='LocationID', primary_key=True)  # Field name made lowercase.
    locationname = models.CharField(db_column='LocationName', max_length=50)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Location_Master'


class MediaMaster(models.Model):
    mediaid = models.AutoField(db_column='MediaID', primary_key=True)  # Field name made lowercase.
    mediatype = models.CharField(db_column='MediaType', max_length=25, blank=True, null=True)  # Field name made lowercase.
    mediaurl = models.TextField(db_column='MediaUrl', blank=True, null=True)  # Field name made lowercase.
    isactive = models.IntegerField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    lastbrodcasteddate = models.DateTimeField(db_column='LastBrodcastedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Media_Master'

class PostImage(models.Model):
    title = models.CharField(max_length=150)
    cover = models.ImageField(upload_to='images/')
   
    def __str__(self):
        return self.title

class WebphoneUsers(models.Model):
    wpid = models.AutoField(primary_key=True)
    cam_id = models.IntegerField(blank=True, null=True)
    wp_server_name = models.CharField(max_length=50, blank=True, null=True)
    wp_user_name = models.CharField(max_length=50, blank=True, null=True)
    wp_user_password = models.CharField(max_length=50, blank=True, null=True)
    wp_user_status = models.IntegerField(blank=True, null=True)
    wp_user_created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'webphone_users'
