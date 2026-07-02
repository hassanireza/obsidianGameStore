import pytest
from django.urls import reverse
from store.models import Genre, Game


@pytest.mark.django_db
def test_game_str():
    genre = Genre.objects.create(name='Puzzle', slug='puzzle')
    game = Game.objects.create(
        slug='test-game', name='Test Game', tagline='A test',
        description='desc', genre=genre, game_folder='testgame'
    )
    assert str(game) == 'Test Game'


@pytest.mark.django_db
def test_home_page_loads(client):
    response = client.get(reverse('home'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_catalog_page_loads(client):
    response = client.get(reverse('store:catalog') if 'store' in reverse.__module__ else reverse('catalog'))
    assert response.status_code == 200
