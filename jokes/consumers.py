from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class JokesConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)("jokes", self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("jokes", self.channel_name)

    def jokes_joke(self, event):
        self.send(text_data=event["text"])
