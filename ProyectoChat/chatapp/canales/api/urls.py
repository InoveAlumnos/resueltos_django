from django.urls import path, include

# Importamos las API_VIEWS:
from canales.api.views import *


urlpatterns = [
    path('login/', LoginUserAPIView.as_view(), name="login"),

    # Include router:
    path('canales/', include('canales.api.routers')), 
    
    # Chat-Mensajes:
    path(
        'chats/<int:pk>/mensajes/',
        ChatMensajesAPIView.as_view(),
        name='chat-list-mensajes'
    ),
    
    # Chat-Mensajes-usuario:
    path(
        'chats/<int:pk>/mensajes/<str:username>/',
        ChatMensajesUserAPIView.as_view(),
        name='chat-list-mensajes-usuario'
    ),
]
