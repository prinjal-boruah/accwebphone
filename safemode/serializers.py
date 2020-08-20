from rest_framework import serializers
from .models import *

class MediaContentSerializer(serializers.ModelSerializer):
    class Meta:
        model=MediaContent
        fields= ("media_type","url","user_id") 