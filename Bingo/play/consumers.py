# play/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer

class WaitRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Conectar al grupo de la sala de espera
        self.room_name = "wait_room"
        self.room_group_name = f"play_{self.room_name}"

        # Unir al grupo de la sala de espera
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Dejar el grupo de la sala de espera
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Recibir un mensaje del WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json.get("action", None)

        if action == "get_user_count":
            # Obtener el número de usuarios conectados
            channel_layer = get_channel_layer()
            group_channels = await channel_layer.group_channels(self.room_group_name)
            user_count = len(group_channels)

            # Enviar el número de usuarios a través del WebSocket
            await self.send(text_data=json.dumps({
                'user_count': user_count
            }))
