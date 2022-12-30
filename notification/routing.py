from django.urls import path
from . import client

websocket_urlpatterns=[
    path("ws/universal/",client.Notification.as_asgi()),
]