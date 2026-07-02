import pytest
from django.urls import reverse
from store.models import Genre, Game


@pytest.fixture
def game(db):
    genre = Genre.objects.create(name='Puzzle', slug='puzzle')
    return Game.objects.create(
        slug='test-game', name='Test Game', tagline='A test tagline',
        description='A test description', genre=genre, game_folder='testgame'
    )


def test_game_str(game):
    assert str(game) == 'Test Game'


def test_genre_str(db):
    genre = Genre.objects.create(name='Action', slug='action')
    assert str(genre) == 'Action'


def test_home_page_loads(client):
    response = client.get(reverse('home'))
    assert response.status_code == 200


def test_catalog_page_loads(client):
    response = client.get(reverse('catalog'))
    assert response.status_code == 200


def test_game_detail_page_loads(client, game):
    response = client.get(reverse('game_detail', args=[game.slug]))
    assert response.status_code == 200


def test_game_detail_404_for_missing_slug(client):
    response = client.get(reverse('game_detail', args=['nonexistent']))
    assert response.status_code == 404


def test_play_game_increments_plays(client, game):
    assert game.plays == 0
    client.get(reverse('play_game', args=[game.slug]))
    game.refresh_from_db()
    assert game.plays == 1


def test_toggle_wishlist_requires_login(client, game):
    response = client.post(reverse('toggle_wishlist', args=[game.slug]))
    assert response.status_code == 401
