from flask import Flask, render_template, request
import json
import csv

# Create an instance of the Flask class
app = Flask(__name__)

# Function to read JSON data from a file
def read_json(file_path):
    with open(file_path) as f:
        return json.load(f)

# Function to read CSV data from a file and convert to a list of dictionaries
def read_csv(file_path):
    products = []
    with open(file_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert id to integer and price to float
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

# Define the route for displaying products
@app.route('/products')
def products():
    # Get the source and product ID from query parameters
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []
    error_message = None
    
    # Determine the source of the data (JSON or CSV)
    if source == 'json':
        try:
            # Read products from the JSON file
            products = read_json('products.json')
        except FileNotFoundError:
            error_message = "JSON file not found."
    elif source == 'csv':
        try:
            # Read products from the CSV file
            products = read_csv('products.csv')
        except FileNotFoundError:
            error_message = "CSV file not found."
    else:
        error_message = "Wrong source"

    # Filter products by ID if provided
    if not error_message and product_id:
        try:
            product_id = int(product_id)
            # Filter the list of products to find the one with the specified ID
            products = [product for product in products if product['id'] == product_id]
            if not products:
                error_message = "Product not found"
        except ValueError:
            error_message = "Invalid id"

    # Render the 'product_display.html' template with the products and any error message
    return render_template('product_display.html', products=products, error_message=error_message)

# Run the Flask application
if __name__ == '__main__':
    # Enable debug mode and set the port to 5000
    app.run(debug=True, port=5000)
