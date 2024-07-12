#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request
import json

# Create an instance of the Flask class
app = Flask(__name__)

# Define a dictionary to store user information
users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}

# Define the route for the home page
@app.route("/")
def home():
    # Return a welcome message
    return "Welcome to the Flask API!"

# Define the route to get a list of usernames
@app.route("/data")
def data():
    # Return a JSON response containing the list of usernames
    return jsonify(list(users.keys()))

# Define the route to get the status
@app.route("/status")
def status():
    # Return an "OK" message
    return "OK"

# Define the route to get user details by username
@app.route("/users/<username>")
def show_username(username):
    # Return a JSON response with user details for the given username
    return jsonify(users[username])

# Define the route to add a new user
@app.route("/add_user", methods=['POST'])
def add_user():
    # Get the JSON data from the request
    data = request.get_json()
    # Extract the username from the data
    username = data['username']
    # Add the new user to the users dictionary
    users[username] = data
    # Return a JSON response confirming the user was added
    return jsonify({
        "message": "User added",
        "user": data
    }), 201

# Check if this script is being run directly
if __name__ == "__main__":
    # Run the Flask application
    app.run()
