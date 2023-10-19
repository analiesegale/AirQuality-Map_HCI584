# app.py
from flask import Flask, render_template, request
import folium

app = Flask(__name__)

def get_folium_map(city):
    # Get coordinates for the city (you can modify this based on your requirements)
    coordinates = [37.7749, -122.4194]  # Default to San Francisco if city not found

    # Create a Folium map centered at the city's coordinates
    folium_map = folium.Map(location=coordinates, zoom_start=13)

    # Add a marker at the city's coordinates
    folium.Marker(location=coordinates, popup=city).add_to(folium_map)

    return folium_map._repr_html_()

@app.route('/', methods=['GET', 'POST'])
def index():
    map_html = None

    if request.method == 'POST':
        city = request.form['city']
        map_html = get_folium_map(city)

    return render_template('index.html', map_html=map_html)

if __name__ == '__main__':
    app.run(debug=True)
