import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class BreezeConsumer(WebsocketConsumer):
  def connect(self):
    self.group_name = 'test'
    
    async_to_sync(self.channel_layer.group_add)(
      self.group_name,
      self.channel_name
    )
    
    self.accept()

  def receive(self, text_data=None):
    text_data_json = json.loads(text_data)
    message = text_data_json['message']
    print(message)
    
    async_to_sync(self.channel_layer.group_send)(self.group_name, {
      "type": "chat_message",
      "message": "no way!"
    })
    
  def chat_message(self, event):
    message = event['message']
    self.send(text_data=json.dumps({
      "type": "chat",
      "message": message
    }))
  
  # def disconnect(self, code):
  #   return super().disconnect(code)