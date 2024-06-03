from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenido a Catalina Politician Insight SQL"

@app.route('/consulta', methods=['GET'])
def consulta():
    nombre = request.args.get('nombre')
    # Lógica para consultar información del político
    return jsonify({"nombre": nombre, "informacion": "Información del político"})

if __name__ == '__main__':
    app.run(debug=True)

