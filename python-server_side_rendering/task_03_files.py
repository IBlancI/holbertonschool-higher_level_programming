from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json(file_path):
    with open(file_path) as f:
        return json.load(f)

def read_csv(file_path):
    products = []
    with open(file_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []
    error_message = None

    if source == 'json':
        try:
            products = read_json('products.json')
        except FileNotFoundError:
            error_message = "JSON file not found."
    elif source == 'csv':
        try:
            products = read_csv('products.csv')
        except FileNotFoundError:
            error_message = "CSV file not found."
    else:
        error_message = "Wrong source"

    if not error_message and product_id:
        try:
            product_id = int(product_id)
            products = [product for product in products if product['id'] == product_id]
            if not products:
                error_message = "Product not found"
        except ValueError:
            error_message = "Invalid id"

    return render_template('product_display.html', products=products, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
