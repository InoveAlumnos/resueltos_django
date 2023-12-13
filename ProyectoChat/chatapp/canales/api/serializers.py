
# Primero importamos los modelos que queremos serializar:
from canales.models import Chat, Mensaje
from django.contrib.auth.models import User

# Luego importamos todos los serializadores de django rest framework.
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        exclude = ('password',)


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        fields = ('username', 'password')

class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    token = serializers.CharField(source='key', read_only=True)

    class Meta:
        model = Token
        fields = ('user', 'token')
        

class ChatSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Chat
        fields= ('id', 'nombre')
        read_only_fields=('id',)


class MensajeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Mensaje
        fields = ('id', 'user', 'chat', 'contenido', 'creado')
        read_only_fields = ('id', 'creado')
