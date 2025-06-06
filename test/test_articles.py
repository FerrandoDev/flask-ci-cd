import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_articles(client):
    response = client.get('/articles')
    assert response.status_code == 200

    data = response.get_json()
    assert isinstance(data, list)

    for article in data:
        assert 'id' in article
        assert 'titre' in article
        assert 'contenu' in article
        assert 'dt_publication' in article
