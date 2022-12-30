import json
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class Message(models.Model):
    host=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)


@receiver(post_save,sender=Message)
def broadcaste(sender,instance,created,**kwargs):
    channel_layer=get_channel_layer()
    data={'notification':instance.body}
    async_to_sync(channel_layer.group_send)(
        'chat_universal',
        {
            "type":"broadcaste",
            "message":json.dumps(data)
        }
    )
    