# map_display.py
import tkinter as tk
from PIL import Image, ImageTk
import requests
from dotenv import load_dotenv
import os

load_dotenv()

def show_map(latitude, longitude, map_canvas):
    google_maps_api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    map_url = f'https://maps.googleapis.com/maps/api/staticmap?center={latitude},{longitude}&zoom=13&size=300x300&maptype=roadmap&key={google_maps_api_key}'
    
    response = requests.get(map_url, stream=True)
    
    if response.status_code == 200:
        map_image = ImageTk.PhotoImage(Image.open(response.raw).convert("RGB"))
        map_canvas.create_image(0, 0, anchor=tk.NW, image=map_image)
        map_canvas.map_image = map_image  # Keep a reference to prevent garbage collection
    else:
        print(f"Failed to fetch map image. Status code: {response.status_code}")
        hide_map(map_canvas)

def hide_map(map_canvas):
    map_canvas.delete("all")

def create_map_canvas(root):
    map_canvas = tk.Canvas(root, width=300, height=300)
    return map_canvas
