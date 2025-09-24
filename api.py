from flask import Flask, jsonify
import random

# 1. Crea una instancia de la aplicación Flask
app = Flask(__name__)

# 2. Define la ruta de la API, aceptando GET y POST
@app.route('/generate_number', methods=['GET', 'POST'])
def generate_number():
    """Esta función genera un número aleatorio entre 1 y 100."""
    # Genera el número
    random_number = random.randint(1, 100)

    # Devuelve el número en un formato JSON (clave 'number')
    return jsonify({"number": random_number})

# 3. Permite que el script se ejecute directamente (el hosting ignorará el puerto 5000)
if __name__ == '__main__':
    app.run(port=5000, debug=True)