import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    rv = client.get('/')
    assert rv.data == b'Bienvenido a Catalina Politician Insight SQL'

def test_consulta(client):
    rv = client.get('/consulta?nombre=Juan')
    json_data = rv.get_json()
    assert json_data['nombre'] == 'Juan'

