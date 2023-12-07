from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination

from canales.models import Chat, Mensaje
from canales.api.serializers import ChatSerializer, MensajeSerializer

class CustomPagination(PageNumberPagination):
    page_size = 20 # default page size

class ChatViewSet(ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class MensajeViewSet(ModelViewSet):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer
    pagination_class = CustomPagination
    
    def get_queryset(self):
        return self.queryset.order_by("creado")
    

