#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Stockage des utilisateurs en mémoire
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"},
}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    if request.is_json:
        user_data = request.get_json()
        username = user_data.get("username")
        if username in users:
            return jsonify({"error": "User already exists"}), 400
        
        users[username] = {
            "username": username,
            "name": user_data.get("name"),
            "age": user_data.get("age"),
            "city": user_data.get("city"),
        }
        return jsonify({
            "message": "User added",
            "user": users[username]
        }), 201
    else:
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == "__main__":
    app.run(debug=True)