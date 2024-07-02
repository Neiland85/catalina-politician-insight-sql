import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b"Bienvenido a Catalina Politician Insight SQL"

def test_consulta_sin_nombre():
    response = app.test_client().get('/consulta')
    assert response.status_code == 400
    assert b"Nombre del político es requerido" in response.data

def test_consulta_con_nombre():
    response = app.test_client().get('/consulta?nombre=alguien')
    assert response.status_code == 200
    assert b"Consulta exitosa" in response.data

