from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Access the API keys from the environment variables
AIRVISUAL_API_KEY = os.getenv('AIRVISUAL_API_KEY')
GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_air_quality', methods=['POST'])
def get_air_quality():
    city = request.form.get('city')
    state = request.form.get('state')
    country = request.form.get('country')

    # Make a request to the AirVisual API
    airvisual_endpoint = f"http://api.airvisual.com/v2/city?city={city}&state={state}&country={country}&key={AIRVISUAL_API_KEY}"
    response = requests.get(airvisual_endpoint)
    data = response.json()

    if response.status_code == 200:
        air_quality = data['data']['current']['pollution']
        aqi = air_quality['aqius']   
        main_pollutant = air_quality['mainus']

        # Embed Google Map with the provided location
        google_map_url = f"https://www.google.com/maps/embed/v1/place?q={city},{state},{country}&key={GOOGLE_MAPS_API_KEY}"

        return render_template('index.html', aqi=aqi, main_pollutant=main_pollutant, google_map_url=google_map_url)
    else:
        error_message = "Error: Unable to retrieve air quality data."
        return render_template('index.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
