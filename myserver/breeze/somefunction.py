from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()

def runFunction():
  async_to_sync(channel_layer.group_send)("test", {
    "type": "chat_message",
    "message": "no way!"
  })