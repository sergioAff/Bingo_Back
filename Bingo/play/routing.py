# play/routing.py
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/play/wait_room/$', consumers.WaitRoomConsumer.as_asgi()),
]
