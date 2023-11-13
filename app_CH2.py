from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os
import folium

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Access the API keys from the environment variables 
AIRVISUAL_API_KEY = os.getenv("AIRVISUAL_API_KEY")

# get all valid countries, states, cities
def get_countries():
    url = f"http://api.airvisual.com/v2/countries?key={AIRVISUAL_API_KEY}"
    response = requests.get(url, timeout=10)
    data = response.json()
    countries_dict_list = data['data']
    countries_lst = [country_dict['country'] for country_dict in countries_dict_list]
    return countries_lst

def get_states_for_country(country):
    url = f"http://api.airvisual.com/v2/states?country={country}&key={AIRVISUAL_API_KEY}"
    response = requests.get(url, timeout=10)
    data = response.json()
    states_dict_list = data['data']
    states_lst = [state_dict['state'] for state_dict in states_dict_list]
    return states_lst

def get_cities_for_state(state, country):
    url = f"http://api.airvisual.com/v2/cities?state={state}&country={country}&key={AIRVISUAL_API_KEY}"
    response = requests.get(url, timeout=10)
    data = response.json()
    cities_dict_list = data['data']
    cities_lst = [city_dict['city'] for city_dict in cities_dict_list]
    return cities_lst

def geocode_place(place_name): # Ex. Ames, IA  or Berlin, Germany
    # free geocoding service, w/o need for API key!
    base_url = "https://geocode.maps.co/search"  
    params = {"q": place_name}
    
    response = requests.get(base_url, params=params, timeout=10)
    print(response.url)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            # Extract latitude, longitude, and full location name from the first result
            result = data[0]
            lat = result.get("lat")
            lon = result.get("lon")
            location = result.get("display_name")
            return lat, lon, location
    
    # Return None if no data or an error occurred
    return None, None, None



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_air_quality', methods=['POST'])
def get_air_quality():
    city = request.form.get('city').strip() # use strip() to remove leading/trailing whitespace
    state = request.form.get('state').strip()
    country = request.form.get('country').strip()

    # combine city, state, country into a single string and get its lat/long
    place_name = f"{city}, {state}, {country}"
    lat, lon, location = geocode_place(place_name)  

    print("location used:", location)

    # Make a request to the AirVisual API using the lat/lon coordinates
    airvisual_endpoint = f"http://api.airvisual.com/v2/nearest_city?lat={lat}&lon={lon}&key={AIRVISUAL_API_KEY}"
    response = requests.get(airvisual_endpoint, timeout=10)

    if response.status_code == 200:
        data = response.json()
        air_quality = data['data']['current']['pollution']
        aqi = air_quality['aqius']   
        main_pollutant = air_quality['mainus']

        # make a folium map with a marker at the lat/lon coordinates
        folium_map = folium.Map(location=[lat, lon], zoom_start=10)

        # optional: add a pop-up text and tool tip
        html = '<h1>This the location</h1>' # change this to you liking
        popup = folium.Popup(html, max_width=300)
        tooltip = f"{aqi} AQI for {main_pollutant}"

        # add a marker for user location (maybe change icon to something more polluty?
        # Also, you should change the color of the marker based on the AQI value
        folium.Marker([lat, lon], popup=popup, tooltip=tooltip, icon=folium.Icon(color='purple')).add_to(folium_map)

        # convert to html, so we can embed it
        map_html = folium_map._repr_html_()
        return render_template('index.html', aqi=aqi, main_pollutant=main_pollutant, map=map_html)
    else:
        error_message = "Error: Unable to retrieve air quality data."
        return render_template('index.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=False)
