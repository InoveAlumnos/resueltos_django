from django.contrib.auth import authenticate
from django.db.models import Subquery
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
# (GET - ListAPIView) Listar todos los elementos en la entidad:
# (POST - CreateAPIView) Inserta elementos en la DB
# (GET - RetrieveAPIView) Devuelve un solo elemento de la entidad.
# (GET-POST - ListCreateAPIView) Para listar o insertar elementos en la DB
# (GET-PUT - RetrieveUpdateAPIView) Devuelve o actualiza un elemento en particular.
# (DELETE - DestroyAPIView) Permite eliminar un elemento.
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    GenericAPIView,
    UpdateAPIView
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.validators import ValidationError
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication


from canales.api.serializers import *
from canales.models import Chat, Mensaje


class LoginUserAPIView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        # Realizamos validaciones a través del serializador
        user_login_serializer = UserLoginSerializer(data=request.data)
        if user_login_serializer.is_valid():
            _username = request.data.get('username')
            _password = request.data.get('password')

            # Si el usuario existe y sus credenciales son validas,
            # tratamos de obtener el TOKEN:
            _account = authenticate(username=_username, password=_password)
            if _account:
                _token, _created = Token.objects.get_or_create(user=_account)
                return Response(
                    data=TokenSerializer(instance=_token, many=False).data,
                    status=status.HTTP_200_OK
                )
            return Response(
                data={'error': 'Invalid Credentials.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            data=user_login_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ChatMensajesAPIView(ListAPIView):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer
    
    def get_queryset(self):
        chat_id = self.kwargs['chat_id']
        queryset = self.queryset.filter(chat_id=chat_id)
        return queryset


class ChatMensajesUserAPIView(ListAPIView):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer
    
    def get_queryset(self):
        chat_id = self.kwargs['chat_id']
        username = self.kwargs['username']
        queryset = self.queryset.filter(chat_id=chat_id, user__username=username)
        return queryset
