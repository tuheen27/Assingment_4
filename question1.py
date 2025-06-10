'''
Create a Flask application with an /api route. When this route is accessed, it should return a JSON list. The data should be stored in a backend file, read from it, and sent as a response.
'''
from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    # Homepage route
    return "<h1>Welcome to Flask API</h1><p>Go to <a href='/api'>/api</a> to see the JSON data</p>"

@app.route('/api', methods=['GET'])
def get_data():
    try:
        # Open and read the JSON file
        with open('data.json', 'r') as file:
            data = json.load(file)  # Load JSON data as a Python list
        return jsonify(data)  # Return as JSON response
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Error handling

@app.errorhandler(404)
def page_not_found(e):
    # Custom 404 handler
    return "<h1>404 - Page Not Found</h1><p>The requested URL was not found on the server.</p><p>Please check the URL or go to <a href='/'>Homepage</a> or <a href='/api'>API</a>.</p>", 404

if __name__ == '__main__':
    app.run(debug=True)
