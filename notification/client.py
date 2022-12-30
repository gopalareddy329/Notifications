import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.contrib.auth.models import User

class Notification(WebsocketConsumer):

    def connect(self):
        self.room_id="universal"
        self.room_group_name="chat_%s" % self.room_id
        async_to_sync (self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
    
    def disconnect(self,event):
         self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
            )
    def broadcaste(self, text_data):
        message=text_data['message']
        print(message)
        self.send(json.dumps({"message":message})
        )
    