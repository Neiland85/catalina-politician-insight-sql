from flask import Flask, request, jsonify
import requests
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    """
    Ruta principal que devuelve un mensaje de bienvenida.
    """
    return "Bienvenido a Catalina Politician Insight SQL"

@app.route('/consulta', methods=['GET'])
def consulta():
    """
    Ruta para consultar información de un político.
    Parámetros:
        nombre (str): Nombre del político a consultar.
    """
    nombre = request.args.get('nombre')
    if not nombre:
        return jsonify({"error": "Nombre del político es requerido"}), 400
    
    # Aquí debería ir la lógica para consultar la información del político
    # Por ejemplo:
    # data = consultar_politico(nombre)
    # if not data:
    #     return jsonify({"error": "Político no encontrado"}), 404

    return jsonify({"mensaje": "Consulta exitosa"})

if __name__ == '__main__':
    app.run(debug=True)

