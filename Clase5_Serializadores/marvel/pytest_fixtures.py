import pytest

from e_commerce.models import Comic


@pytest.fixture
def create_user(django_user_model):
    def make_user(**kwargs):
        return django_user_model.objects.create_user(
            username='inovecode',
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
