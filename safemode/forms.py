from django import forms
from . models import *

class MediaTextContentForm(forms.Form):
    mediatype = forms.CharField(label='mediatype', max_length=150)
    mediaurl = forms.CharField(label='mediaurl', max_length=250)

class ImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields ='__all__'

class IpCamForm(forms.ModelForm):

    class Meta:
        model = Ipcams
        fields = '__all__'

class WebPhoneForm(forms.ModelForm):

    class Meta:
        model = WebphoneUsers
        fields = '__all__'

class MediaMasterForm(forms.ModelForm):

    class Meta:
        model = MediaMaster
        fields = '__all__'