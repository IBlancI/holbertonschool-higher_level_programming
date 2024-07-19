from flask import Flask, render_template

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

# Run the Flask application
if __name__ == '__main__':
    # Enable debug mode and set the port to 5000
    app.run(debug=True, port=5000)
