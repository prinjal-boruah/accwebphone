from django.contrib.auth.models import User
from .models import *

from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .views import *
import datetime


@receiver(post_save, sender=MediaContent)
def announce_new_incident(sender,update_fields,instance,created,**kwargs):
  print(f"sss----------------")
  
  event_name=""

  if instance.media_type == "text":
  	event_name = "New Text"
  	print(f"------New Text----------------")
  elif instance.media_type == "image":
  	event_name = "New Image"
  	print(f"------New Image--------------")
  elif instance.media_type == "animation":
  	event_name = "New Animation"
  	print(f"------New Animation---------------")
  elif instance.media_type == "video":
  	event_name = "New Video"
  	print(f"------New Video---------------")
  elif instance.media_type == "callvideo":
  	event_name = "New Call Video"
  	print(f"------New Call Video---------------")
  elif instance.media_type == "all":
    event_name = "for all"
    print(f"------Stop Event---------------")
  elif instance.media_type == "stop":
  	event_name = "Stop Event"
  	print(f"------Stop Event---------------")
  else:
  	event_name = "Not Correct Event"
  	print(f"------Not Correct Event----------------")

  channel_layer = get_channel_layer()
  async_to_sync(channel_layer.group_send)(
	"gossip", {"type": "user.gossip",
	"event": event_name,
	"media_type": instance.media_type,
  "url": instance.url,
	"user_id": instance.user_id,
	})
