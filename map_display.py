# map_display.py
import folium
from PIL import Image, ImageTk
import io
import tkinter as tk
import requests
from dotenv import load_dotenv
import os

load_dotenv()

class MapDisplay:
    def __init__(self, root):
        self.root = root
        self.map = folium.Map(location=[0, 0], zoom_start=13)
        self.map_canvas = tk.Canvas(root, width=300, height=300)
        self.map_canvas.pack()

    def show_map(self, latitude, longitude):
        google_maps_api_key = os.getenv("GOOGLE_MAPS_API_KEY")
        map_url = f'https://maps.googleapis.com/maps/api/staticmap?center={latitude},{longitude}&zoom=13&size=300x300&maptype=roadmap&key={google_maps_api_key}'

        response = requests.get(map_url, stream=True)

        if response.status_code == 200:
            img = Image.open(io.BytesIO(response.content))
            img = img.resize((300, 300), Image.ANTIALIAS)
            tk_image = ImageTk.PhotoImage(img)
            self.map_canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
            self.map_canvas.map_image = tk_image  # Keep a reference to prevent garbage collection
        else:
            print(f"Failed to fetch map image. Status code: {response.status_code}")
            self.hide_map()

    def hide_map(self):
        self.map_canvas.delete("all")
