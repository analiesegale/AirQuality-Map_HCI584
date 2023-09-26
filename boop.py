import tkinter as tk
import requests
from tkinter import messagebox

# Function to fetch air quality data
def get_air_quality(latitude, longitude):
    api_url = f'https://api.waqi.info/feed/geo:{latitude};{longitude}/?token=7773a303cb7f1a0924970069bcf80b415e0876d5'
    
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

# Function to update the air quality value
def update_air_quality():
    location_str = address_entry.get()
    try:
        # Split the input into latitude and longitude
        latitude, longitude = map(float, location_str.split(","))
        
        air_quality_value = get_air_quality(latitude, longitude)

        if air_quality_value is not None:
            air_quality_label.config(text=f'Air Quality Index: {air_quality_value}')
        else:
            air_quality_label.config(text="Failed to retrieve air quality data.")
    except ValueError:
        air_quality_label.config(text="Invalid input format. Please enter latitude and longitude separated by a comma (e.g., 40.7128,-74.0060).")

# Create the main application window
root = tk.Tk()
root.title("Air Quality App")

# Label and entry for the user to input latitude and longitude
address_label = tk.Label(root, text="Enter latitude and longitude:")
address_label.pack()
address_entry = tk.Entry(root)
address_entry.pack()

# Button to update the air quality
update_button = tk.Button(root, text="Update Air Quality", command=update_air_quality)
update_button.pack()

# Label to display the air quality value
air_quality_label = tk.Label(root, text="")
air_quality_label.pack()

root.mainloop()
