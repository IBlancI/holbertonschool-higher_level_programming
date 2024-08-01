#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Define the hostname and port for the server
HOSTNAME = 'localhost'
PORT = 8000

# Create a custom HTTP request handler class
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # Handle GET requests
    def do_GET(self):
        # Check the requested path
        if self.path == "/":
            # Send a 200 OK response
            self.send_response(200)
            # Specify the content type as plain text
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            # Write the response message
            self.wfile.write("Hello, this is a simple API!", encoding='utf8')

        elif self.path == "/data":
            # Send a 200 OK response
            self.send_response(200)
            # Specify the content type as JSON
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            # Define the data to be returned as JSON
            data = {"name": "John", "age": 30, "city": "New York"}
            # Write the JSON response
            self.wfile.write(json.dumps(data), encoding='utf-8')

        elif self.path == "/status":
            # Send a 200 OK response
            self.send_response(200)
            # Specify the content type as plain text
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            # Write the response message
            self.wfile.write("OK", encoding='utf8')

        elif self.path == "/info":
            # Send a 200 OK response
            self.send_response(200)
            # Specify the content type as JSON
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            # Define the information to be returned as JSON
            info = {"version": "1.0",
                    "description": "A simple API built with http.server"}
            # Write the JSON response
            self.wfile.write(json.dumps(info), encoding='utf-8')

        else:
            # Send a 404 Not Found response for unknown paths
            self.send_response(404)
            # Specify the content type as plain text
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            # Write the response message
            self.wfile.write("Endpoint not found", encoding='utf8')

# Function to start and run the server
def run(server_class=HTTPServer,
        handler_class=SimpleHTTPRequestHandler,
        hostname=HOSTNAME, port=PORT):
    # Define the server address
    server_address = (hostname, port)
    # Create an HTTP server instance
    httpd = server_class(server_address, handler_class)
    # Print a message indicating the server is starting
    print(f"Starting server on port {port}...")
    # Run the server indefinitely
    httpd.serve_forever()

# Check if this script is being run directly
if __name__ == "__main__":
    # Start the server
    run()
