# app.py
from flask import Flask, render_template, request, make_response
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Load the Google Maps API key from the .env file
GOOGLE_MAPS_API_KEY = os.environ.get("GOOGLE_MAPS_API_KEY")

# OpenAQ API endpoint (v2)
OPENAQ_API_URL = "https://api.openaq.org/v2/measurements"

# Use os.environ to access environment variables
OPENAQ_API_KEY = os.environ.get("OPENAQ_API_KEY")

@app.route('/')
def index():
    last_entered_city = request.cookies.get('lastEnteredCity', '')
    return render_template('index.html', air_quality=None, last_entered_city=last_entered_city, google_maps_api_key=GOOGLE_MAPS_API_KEY)

@app.route('/air_quality', methods=['POST'])
def get_air_quality():
    city = request.form.get('city')

    if not city:
        last_entered_city = request.cookies.get('lastEnteredCity', '')  # Retrieve last entered city
        return render_template('index.html', air_quality="Please provide a city.", last_entered_city=last_entered_city)

    air_quality, last_entered_city = get_air_quality_data(city)

    # Store the last entered city in a cookie
    response = make_response(render_template('index.html', air_quality=air_quality, last_entered_city=last_entered_city))
    response.set_cookie('lastEnteredCity', last_entered_city)

    return response

def get_air_quality_data(city):
    # Define parameters for the OpenAQ API request
    params = {
        'city[]': city,
        'country[]': 'US',
        'limit': 1,
        'parameter[]': 'pm25',
    }

    if OPENAQ_API_KEY:
        params['key'] = OPENAQ_API_KEY

    response = requests.get(OPENAQ_API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        if data['results']:
            value = data['results'][0]['value']
            air_quality = f"The PM2.5 air quality in {city} is {value} µg/m³."
            return air_quality, city
        else:
            return f"No air quality data found for {city}.", city
    else:
        return f"Error fetching air quality data: {response.status_code}", city

if __name__ == '__main__':
    app.run(debug=True)
