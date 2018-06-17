from channels.routing import ProtocolTypeRouter, URLRouter
import jokes.routing

application = ProtocolTypeRouter(
    {"websocket": URLRouter(jokes.routing.websocket_urlpatterns)}
)
