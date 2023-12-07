from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Chat(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=60)


class Mensaje(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    contenido = models.CharField(max_length=300)
    creado = models.DateTimeField(auto_now_add=True)
