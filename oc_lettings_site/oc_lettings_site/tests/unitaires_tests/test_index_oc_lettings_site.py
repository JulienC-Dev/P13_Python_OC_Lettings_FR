from django.urls import reverse


def test_view_index_oc_status(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


def test_view_index_oc_title(client):
    url = reverse('indexfdd')
    response = client.get(url)
    assert '<title>Holiday Homes</title>' in str(response.content)
