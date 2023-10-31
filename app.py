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
        last_entered_city = request.cookies.get('lastEnteredCity', '')  # Retrieve the last entered city
        return render_template('index.html', air_quality="Please provide a city.", last_entered_city=last_entered_city)

    air_quality, aqi_value, color, health_impact, caution = get_air_quality_data(city)

    # Store the last entered city in a cookie
    response = make_response(render_template('index.html', air_quality=air_quality, last_entered_city=city, aqi_value=aqi_value, color=color, health_impact=health_impact, caution=caution))
    response.set_cookie('lastEnteredCity', city)

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
            air_quality, color, health_impact, caution = get_aqi_info(value)  # Pass the AQI value to get_aqi_info
            return air_quality, value, color, health_impact, caution
        else:
            return f"No air quality data found for {city}.", 0, 'gray', '', ''
    else:
        return f"Error fetching air quality data: {response.status_code}", 0, 'gray', '', ''

def get_aqi_info(aqi_value):
    if aqi_value <= 50:
        color = 'green'
        health_impact = 'Good'
        caution = 'Air quality is satisfactory, and air pollution poses little or no risk.'
    elif aqi_value <= 100:
        color = 'yellow'
        health_impact = 'Moderate'
        caution = 'Air quality is acceptable; however, some pollutants may be a concern for a small number of people who are unusually sensitive to air pollution.'
    elif aqi_value <= 150:
        color = 'orange'
        health_impact = 'Unhealthy for Sensitive Groups'
        caution = 'Members of sensitive groups may experience health effects, but the general public is less likely to be affected.'
    elif aqi_value <= 200:
        color = 'red'
        health_impact = 'Unhealthy'
        caution = 'Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.'
    elif aqi_value <= 300:
        color = 'purple'
        health_impact = 'Very Unhealthy'
        caution = 'Health alert: everyone may experience more serious health effects.'
    else:
        color = 'maroon'
        health_impact = 'Hazardous'
        caution = 'Health warning of emergency conditions: the entire population is more likely to be affected.'

    air_quality = f"The PM2.5 air quality in this area is {aqi_value} µg/m³."
    return air_quality, color, health_impact, caution

if __name__ == '__main__':
    app.run(debug=True)
