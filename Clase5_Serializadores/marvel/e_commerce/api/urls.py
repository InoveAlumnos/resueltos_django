from django.urls import path
from e_commerce.marvel_views import *

# Importamos las API_VIEWS:
from e_commerce.api.views import *


urlpatterns = [
    # Comic Function API View:
    path('comic-list/', comic_list_api_view),
    path('comic-retrieve/', comic_retrieve_api_view),
    path('comic-create/', comic_create_api_view),
    # Comic Class API View:
    path('comics/list/', GetComicAPIView.as_view()),
    path('comics/<int:pk>/', GetOneComicAPIView.as_view()),
    path(
        'comics/<int:marvel_id>/',
        GetOneMarvelComicAPIView.as_view()
    ),
    path('comics/create/', PostComicAPIView.as_view()),
    path('comics/list-create/', ListCreateComicAPIView.as_view()),
    path('comics/update/<int:marvel_id>/', UpdateComicAPIView.as_view()),
    path(
        'comics/retrieve-update/<int:pk>/',
        RetrieveUpdateComicAPIView.as_view()
    ),
    path('comics/delete//<int:pk>/', DestroyComicAPIView.as_view()),
    # TODO: User Class API View.
    path(
        'users/list/',
        UserListAPIView.as_view(),
        name='user_class_list_api_view'
    ),
    path(
        'users/<str:username>/',
        UserRetrieveAPIView.as_view(),
        name='user_class_retrieve_api_view'
    ),
    # TODO: Wish-list Class API View.
    path(
        'wish/list-create/',
        WishListAPIView.as_view(),
        name='wishlist_class_api_view'
    ),
]
