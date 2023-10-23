from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# OpenAQ API endpoint (v2)
OPENAQ_API_URL = "https://api.openaq.org/v2/measurements"

# Use os.environ to access environment variables
OPENAQ_API_KEY = os.environ.get("OPENAQ_API_KEY")

@app.route('/')
def index():
    return render_template('index.html', air_quality=None, last_entered_city=get_last_entered_city())

@app.route('/air_quality', methods=['POST'])
def get_air_quality():
    city = request.form.get('city')

    if not city:
        return render_template('index.html', air_quality="Please provide a city.", last_entered_city=get_last_entered_city())

    air_quality, last_entered_city = get_air_quality_data(city)

    return render_template('index.html', air_quality=air_quality, last_entered_city=last_entered_city)

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
            set_last_entered_city(city)  # Store the last entered city in local storage
            return air_quality, city
        else:
            return f"No air quality data found for {city}.", city
    else:
        return f"Error fetching air quality data: {response.status_code}", city

def set_last_entered_city(city):
    # Set the last entered city in local storage using JavaScript
    script = f"<script>localStorage.setItem('lastEnteredCity', '{city}');</script>"
    return script

def get_last_entered_city():
    # Retrieve the last entered city from local storage using JavaScript
    script = "<script>const lastEnteredCity = localStorage.getItem('lastEnteredCity'); lastEnteredCity;</script>"
    return script

if __name__ == '__main__':
    app.run(debug=True)
