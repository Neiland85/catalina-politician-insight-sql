import sys
import os

# Insertar la ruta del directorio principal del proyecto
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b"Bienvenido a Catalina Politician Insight SQL"

