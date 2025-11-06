from flask import Flask, jsonify, request
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

usuarios = []

@app.route("/health")
def health():
    return { "status": "ok" }, 200

@app.route("/users", methods=["POST"])
def create_user():
        data = request.get_json()
        nome = data.get("nome")

        if not nome:
            app.logger.info("failed to login: nome is missing")
            return jsonify({ "error": "Nome is required" }), 400
        
        usuarios.append(nome)
        app.logger.info(f"added to users {nome}")
        return jsonify ({
            "message": "Usuario Adicionado",
            "usuarios": usuarios
        }), 201
        
    
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify({"usuarios": usuarios}), 200

