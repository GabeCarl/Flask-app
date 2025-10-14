from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = []

@app.route("/health")
def health():
    return { "status": "ok" }, 200

@app.route("/user", methods=["POST"])
def create_user():
        data = request.get_json()
        nome = data.get("nome")

        if not nome:
            return jsonify({ "error": "Nome is required" }), 400
        
        usuarios.append(nome)
        return jsonify ({
            "message": "Usuario Adicionado",
            "usuarios": usuarios
        }), 201
    
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify({"usuarios": usuarios}), 200

