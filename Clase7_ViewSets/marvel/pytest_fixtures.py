import pytest
import uuid

from rest_framework.authtoken.models import Token

from e_commerce.models import Comic, WishList


@pytest.fixture
def create_user(django_user_model, username=None):
    def make_user(*args, **kwargs):
        if not username:
            _username = 'inovecode_{}'.format(uuid.uuid4().hex[:6].lower())
        else:
            _username = username
        return django_user_model.objects.create_user(
            username=_username,
            password='12345678hola',
            email='inovecode@mail.com'
        )
    return make_user


@pytest.fixture
def create_comic():
    def make_comic(**kwargs):
        return Comic.objects.create(
            marvel_id=9999,
            title='Inove SuperHeroe',
            description='Coding School',
            price=10.0,
            stock_qty=15,
            picture=''
        )
    return make_comic


@pytest.fixture
def create_wishlist(create_user, create_comic):
    comic = create_comic()
    user = create_user(username='inovecode')
    def make_wishlist(**kwargs):
        return WishList.objects.create(
            user=user,
            comic=comic,
            favorite=True,
            cart=True,
            wished_qty=1,
            bought_qty=0
        )
    return make_wishlist

@pytest.fixture
def get_token(create_user, *args, **kwargs):
    def get_or_create_token(*args, **kwargs):
        token, _ = Token.objects.get_or_create(user=create_user())
        return token
    return get_or_create_token
