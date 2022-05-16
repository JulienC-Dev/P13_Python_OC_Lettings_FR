import pytest
from django.urls import reverse
from profiles.models import Profile


@pytest.mark.django_db
def test_view_index_profiles_status(client):
    url = reverse('profiles_index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_view_index_profiles_title(client):
    url = reverse('profiles_index')
    response = client.get(url)
    assert '<title>Profiles</title>' in str(response.content)


@pytest.mark.django_db
def test_view_profile_status(client):
    profile = Profile.objects.get(user__username="paul")
    url = reverse('profile', kwargs={'username': profile.user.username})
    response = client.get(url)
    assert response.status_code == 200
    assert profile.user.username == 'paul'
    profile = Profile.objects.all()
    assert profile.count() == 1


@pytest.mark.django_db
def test_view_profile_title(client):
    profile = Profile.objects.get(user__username="paul")
    url = reverse('profile', kwargs={'username': profile.user.username})
    response = client.get(url)
    assert f'<title>{profile.user.username}</title>' in str(response.content)
