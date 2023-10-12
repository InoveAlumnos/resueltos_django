import pytest

from e_commerce.models import Comic, WishList


@pytest.fixture
def create_user(db, django_user_model):
    def make_user(**kwargs):
        return django_user_model(
            username='root',
            password='12345678hola',
            email='root@gmail.com'
        )
    return make_user


@pytest.fixture
def create_comic():
    def make_comic(**kwargs):
        return Comic(
            marvel_id=1010,
            title='Inove SuperHeroe',
            description='Coding School',
            price=10.0,
            stock_qty=15,
            picture=''
        )
    return make_comic


@pytest.fixture
def create_wishlist(db, wishlist_model):
    def make_wishlist(**kwargs):
        return wishlist_model(**kwargs)
    return make_wishlist
