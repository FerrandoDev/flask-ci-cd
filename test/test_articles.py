from unittest.mock import patch
from flask.testing import FlaskClient

@patch('app.routes.mysql.connector.connect')
def test_get_articles(mock_connect, client: FlaskClient):
    mock_conn = mock_connect.return_value
    mock_cursor = mock_conn.cursor.return_value
    mock_cursor.fetchall.return_value = [(1, "Titre de test", "Contenu de test")]

    response = client.get('/articles')
    assert response.status_code == 200
    assert b'Titre de test' in response.data
