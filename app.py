from flask import Flask, request, jsonify

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
    Retorna:
        JSON: Información del político.
    """
    nombre = request.args.get('nombre')
    
    if not nombre:
        return jsonify({"error": "Nombre del político es requerido"}), 400
    
    try:
        # Lógica para consultar información del político
        informacion_politico = obtener_informacion_politico(nombre)
        return jsonify({"nombre": nombre, "informacion": informacion_politico})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def obtener_informacion_politico(nombre):
    """
    Función ficticia para obtener información de un político.
    Parámetros:
        nombre (str): Nombre del político.
    Retorna:
        str: Información del político.
    """
    # Aquí iría la lógica real para obtener información del político
    return "Información detallada del político"

if __name__ == '__main__':
    app.run(debug=True)
