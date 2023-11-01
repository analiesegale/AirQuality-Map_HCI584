from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Access the API key from the environment variables
AIRVISUAL_API_KEY = os.getenv('AIRVISUAL_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_air_quality', methods=['POST'])
def get_air_quality():
    city = request.form.get('city')
    state = request.form.get('state')
    country = request.form.get('country')

    # Make a request to the AirVisual API
    endpoint = f"http://api.airvisual.com/v2/city?city={city}&state={state}&country={country}&key={AIRVISUAL_API_KEY}"
    print(endpoint)
    response = requests.get(endpoint)
    data = response.json()

    if response.status_code == 200:
        air_quality = data['data']['current']['pollution']
        aqi = air_quality['aqius']
        main_pollutant = air_quality['mainus']
        return render_template('index.html', aqi=aqi, main_pollutant=main_pollutant)
    else:
        error_message = "Error: Unable to retrieve air quality data."
        return render_template('index.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
