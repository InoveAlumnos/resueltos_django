import pytest
import uuid

from rest_framework.authtoken.models import Token
from rest_framework import serializers

from canales import models

@pytest.fixture
def get_token(create_user, *args, **kwargs):
    def get_or_create_token(*args, **kwargs):
        token, _ = Token.objects.get_or_create(user=create_user())
        return token
    return get_or_create_token

@pytest.fixture
def create_user(django_user_model, username=None):
    def make_user(*args, **kwargs):
        if not username:
            _username = f'inovecode_{uuid.uuid4().hex[:6].lower()}'
        else:
            _username = username
        return django_user_model.objects.create_user(
            username=_username,
            password='12345678hola',
            email='inovecode@mail.com'
        )
    return make_user

@pytest.fixture
def create_chat():
    def make_chat(**kwargs):
        if hasattr(models, 'Chat'):
            return models.Chat.objects.create(
                nombre=f'chat_{uuid.uuid4().hex[:6].lower()}'
            )
        else:
            return None
    return make_chat

@pytest.fixture
def create_mensaje(create_user, create_chat):
    chat = create_chat()
    user = create_user(username='inovecode')
    def make_mensaje(**kwargs):
        if hasattr(models, 'Mensaje'):
            return models.Mensaje.objects.create(
                user=user,
                chat=chat,
                contenido=f'Mensaje de prueba {uuid.uuid4().hex[:6].lower()}'
            )
        else:
            return None
    return make_mensaje

@pytest.fixture
def serialize_mensaje(*args, **kwargs):
    def serialize(mensaje):
        if hasattr(models, 'Mensaje'):
            class TestMensajeSerializer(serializers.ModelSerializer):
                class Meta:
                    model = models.Mensaje
                    fields = ('id', 'user', 'chat', 'contenido', 'creado')
                    read_only_fields = ('id', 'creado')
            return TestMensajeSerializer(mensaje).data
        else:
            return None
    return serialize
