from django.contrib.auth import get_user_model

# Primero importamos los modelos que queremos serializar:
from e_commerce.models import Comic, WishList

# Luego importamos todos los serializadores de django rest framework.
from rest_framework import serializers


User = get_user_model()


class ComicSerializer(serializers.ModelSerializer):
    # new_field = serializers.SerializerMethodField()

    # def get_new_field(self, obj):
    #     return {'message': 'Acá puedo devolver más información.'}

    class Meta:
        model = Comic
        fields = '__all__'
        # fields = ('marvel_id', 'title', 'new_field')
        read_only_fields = ('id',)


# TODO: Realizar el serializador para el modelo de User y WishList.
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class WishListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WishList
        fields = '__all__'
