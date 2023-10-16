import requests
from dotenv import load_dotenv
import os
from map_display import MapDisplay

load_dotenv()

def get_coordinates_from_city(city):
    GEOCODING_API = os.getenv("GEOCODING_API")
    geocoding_url = f'https://api.api-ninjas.com/v1/geocoding?city={city}'
    
    try:
        response = requests.get(geocoding_url, headers={'X-Api-Key': GEOCODING_API})
        data = response.json()
        
        if isinstance(data, list) and len(data) > 0:
            result = data[0]
            return result.get('latitude'), result.get('longitude')
        else:
            return None, None
    except Exception as e:
        print(e)
        return None, None

def get_air_quality(latitude, longitude):
    AQ_API = os.getenv("AQ_API")
    api_url = f'https://api.waqi.info/feed/geo:{latitude};{longitude}/?token={AQ_API}'
    
    try:
        response = requests.get(api_url)
        data = response.json()
        if 'data' in data:
            return data['data']['aqi']
        else:
            return None
    except Exception as e:
        print(e)
        return None

def update_air_quality(address_entry, map_display, air_quality_label):
    city = address_entry.get()
    try:
        latitude, longitude = get_coordinates_from_city(city)
        
        if latitude is not None and longitude is not None:
            air_quality_value = get_air_quality(latitude, longitude)

            if air_quality_value is not None:
                air_quality_label.config(text=f'Air Quality Index: {air_quality_value}')
                map_display.show_map(latitude, longitude)
            else:
                air_quality_label.config(text="Failed to retrieve air quality data.")
                map_display.hide_map()
        else:
            air_quality_label.config(text="Failed to retrieve coordinates for the given city.")
            map_display.hide_map()
    except ValueError:
        air_quality_label.config(text="Invalid input. Please enter a valid city.")
        map_display.hide_map()
