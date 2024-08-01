#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionnaire pour stocker les utilisateurs
users = {}

# Route pour la page d'accueil
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Flask API!"

# Route pour récupérer les noms d'utilisateur
@app.route('/data', methods=['GET'])
def get_users():
    return jsonify(list(users.keys()))

# Route pour vérifier le statut de l'API
@app.route('/status', methods=['GET'])
def status():
    return "OK"

# Route pour récupérer un utilisateur par nom d'utilisateur
@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Route pour ajouter un nouvel utilisateur
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    username = data.get('username')
    
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201

# Exécutez l'application Flask
if __name__ == "__main__":
    app.run(debug=True)
