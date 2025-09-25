import os
from flask import Flask, jsonify
import random

# 1. Crea una instancia de la aplicación Flask
app = Flask(__name__)

# 2. Define la ruta de la API (Endpoint)
# Usaremos la ruta que tenías originalmente: /generate_number
# Aceptamos tanto GET (navegador) como POST (AppSheet)
@app.route('/generate_number', methods=['GET', 'POST'])
def generate_number():
    """Esta función genera un número aleatorio entre 1 y 100."""
    
    # Genera el número
    random_number = random.randint(1, 100)
    
    # Devuelve el número en un formato JSON (clave 'number')
    return jsonify({"number": random_number})

# 3. Inicia la aplicación usando el puerto asignado por Render (la clave del despliegue)
if __name__ == '__main__':
    # Lee la variable de entorno 'PORT'. Si Render no la proporciona, usa 5000 como fallback.
    # El host '0.0.0.0' es necesario para escuchar peticiones externas en la nube.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)