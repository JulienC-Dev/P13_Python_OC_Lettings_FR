import pytest
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.fixture(scope='module')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        user = User.objects.create_user(username="paul", email="paul@yahoo.fr",
                                        password="test321321")
        Profile.objects.create(user=user, favorite_city="Paris")
