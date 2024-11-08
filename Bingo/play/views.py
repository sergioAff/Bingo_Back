# views.py
from django.http import JsonResponse
from channels.layers import get_channel_layer
import asyncio

async def get_user_count(request):
    # Aquí, obtener el número de usuarios conectados usando Channel Layer (Redis)
    channel_layer = get_channel_layer()
    room_name = "prueba1"
    
    # Obtener todos los canales en el grupo
    group_channels = await channel_layer.group_channels(room_name)
    user_count = len(group_channels)
    
    return JsonResponse({'user_count': user_count})
