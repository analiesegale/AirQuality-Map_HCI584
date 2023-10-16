# map_display.py
import tkinter as tk
from PIL import Image, ImageTk
import requests
from dotenv import load_dotenv
import os

class MapDisplay:
    def __init__(self, root):
        load_dotenv()
        self.root = root
        self.map_canvas = self._create_map_canvas()

    def show_map(self, latitude, longitude):
        google_maps_api_key = os.getenv("GOOGLE_MAPS_API_KEY")
        map_url = f'https://maps.googleapis.com/maps/api/staticmap?center={latitude},{longitude}&zoom=13&size=300x300&maptype=roadmap&key={google_maps_api_key}'

        response = requests.get(map_url, stream=True)

        if response.status_code == 200:
            map_image = ImageTk.PhotoImage(Image.open(response.raw).convert("RGB"))
            self.map_canvas.create_image(0, 0, anchor=tk.NW, image=map_image)
            self.map_canvas.map_image = map_image  # Keep a reference to prevent garbage collection
        else:
            print(f"Failed to fetch map image. Status code: {response.status_code}")
            self.hide_map()

    def hide_map(self):
        self.map_canvas.delete("all")

    def _create_map_canvas(self):
        map_canvas = tk.Canvas(self.root, width=300, height=300)
        return map_canvas
