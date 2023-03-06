from flask import Flask, jsonify
import shodan
from shodanplayground import search_shodan

app = Flask(__name__)

# Set up your Shodan API key
SHODAN_API_KEY = 'your_api_key_here'
api = shodan.Shodan(SHODAN_API_KEY)

# Define your Flask route
@app.route('/shodan/<query>')
def shodan_search(query):
    try:
        # Use your search_shodan function to search for the query
        results = search_shodan(api, query)

        # Convert the results to a JSON object and return it
        return jsonify({'results': results})
    except shodan.exception.APIError as e:
        # If there's an error, return a 500 status code and an error message
        return jsonify({'error': str(e)}), 500
