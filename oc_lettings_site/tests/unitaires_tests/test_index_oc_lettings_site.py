from django.urls import reverse


def test_view_index_profiles_status(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
