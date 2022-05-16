import pytest
from lettings.models import Letting
from django.urls import reverse


@pytest.mark.django_db
def test_view_index_letting_status(client):
    url = reverse('lettings_index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_view_index_letting_title(client):
    url = reverse('lettings_index')
    response = client.get(url)
    assert '<title>Lettings</title>' in str(response.content)


@pytest.mark.django_db
def test_view_letting_status(client):
    letting = Letting.objects.get(id=1)
    url = reverse('letting', kwargs={'letting_id': letting.id})
    response = client.get(url)
    assert response.status_code == 200
    assert letting.title == 'Location du soleil'
    letting = Letting.objects.all()
    assert letting.count() == 1


@pytest.mark.django_db
def test_view_letting_title(client):
    letting = Letting.objects.get(id=1)
    url = reverse('letting', kwargs={'letting_id': letting.id})
    response = client.get(url)
    assert f'<title>{letting.title}</title>' in str(response.content)
