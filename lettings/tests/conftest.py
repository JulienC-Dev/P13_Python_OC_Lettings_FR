import pytest
from lettings.models import Address, Letting


@pytest.fixture(scope='module')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        address = Address.objects.create(number=300, street="rue de pierre", city="chelles", state="FR", zip_code=77500,
                         country_iso_code="FRA")
        Letting.objects.create(title="Location du soleil", address=address)

