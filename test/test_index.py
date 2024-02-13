import pytest
from datetime import datetime
from app import app, loadClubs, loadCompetitions

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    # Chargement des clubs et des compétitions depuis le JSON
    competitions = loadCompetitions(datetime.strptime("2024-02-12 09:00:00", "%Y-%m-%d %H:%M:%S"))
    clubs = loadClubs()
    # Send a GET request to the index route
    response = client.get('/')

        # Vérification que le code de statut de la réponse est 200 (OK)
    assert response.status_code == 200

        # Vérification que la réponse contient les données attendues des compétitions et des clubs
    for competition in competitions:
        assert bytes(competition['name'], 'utf-8') in response.data

    for club in clubs:
        assert bytes(club['name'], 'utf-8') in response.data
