from flask import Flask, render_template
import json

# Create an instance of the Flask class
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    # Render the 'index.html' template for the home page
    return render_template('index.html')

# Define the route for the about page
@app.route('/about')
def about():
    # Render the 'about.html' template for the about page
    return render_template('about.html')

# Define the route for the contact page
@app.route('/contact')
def contact():
    # Render the 'contact.html' template for the contact page
    return render_template('contact.html')

# Define the route for the items page
@app.route('/items')
def items():
    try:
        # Open and load the JSON data from 'items.json'
        with open('items.json') as f:
            data = json.load(f)
        # Retrieve the list of items from the JSON data
        items_list = data.get("items", [])
    except FileNotFoundError:
        # Handle the case where the 'items.json' file is not found
        items_list = []
    # Render the 'items.html' template and pass the list of items
    return render_template('items.html', items=items_list)

# Run the Flask application
if __name__ == '__main__':
    # Enable debug mode and set the port to 5000
    app.run(debug=True, port=5000)
