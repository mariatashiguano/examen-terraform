from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app) 

@app.route('/')
def hello():
    return jsonify({
        "message": "¡Hola desde el Backend (Lab A)!",
        "status": "Healthy",
        "infra": "AWS ASG + Docker"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)