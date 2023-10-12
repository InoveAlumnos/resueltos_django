from django.urls import path

from e_commerce.views import *

urlpatterns = [
    path('create_comic/', create_comic_view, name='create_comic_view'),
]