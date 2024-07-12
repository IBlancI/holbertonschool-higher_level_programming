#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

# Create an instance of the Flask class
app = Flask(__name__)

# Set configuration for the Flask app
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

# Create instances for HTTP Basic Auth and JWT Auth
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Define a dictionary to store user information with hashed passwords
users = {
    "Adil": {
        "username": "Adil",
        "password": generate_password_hash("password"),
        "role": "admin"
    },
    "Adil93grrrr": {
        "username": "Adil93grrrr",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "EZWin": {
        "username": "EZWin",
        "password": generate_password_hash("password"),
        "role": "user"
    }
}

# Define a function to verify the user's password
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user

# Define a route protected with basic authentication
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

# Define a route for user login to generate a JWT token
@app.route('/login', methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity={
            "username": username,
            "role": user['role']
        })
        return jsonify({"access_token": access_token})
    return jsonify({"error": "Invalid credentials"}), 401

# Define a route protected with JWT authentication
@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

# Define a route that only allows admin access
@app.route('/admin-only')
@jwt_required()
def admin_only():
    user = get_jwt_identity()
    if user['role'] != "admin":
        return jsonify({
            "error": "Permission denied"
        }), 403
    return "Admin Access: Granted"

# Handle errors for missing or invalid JWT tokens
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

# Handle errors for invalid JWT tokens
@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

# Handle errors for expired JWT tokens
@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

# Handle errors for revoked JWT tokens
@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

# Handle errors for tokens that need to be fresh
@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

# Check if this script is being run directly
if __name__ == "__main__":
    # Run the Flask application
    app.run()
