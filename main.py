# main.py
import tkinter as tk
from air_quality import update_air_quality
from map_display import create_map_canvas

root = tk.Tk()
root.title("Air Quality App")

# Label and entry for the user to input city
address_label = tk.Label(root, text="Enter city:")
address_label.pack()
address_entry = tk.Entry(root)
address_entry.pack()

# Create the map canvas
map_canvas = create_map_canvas(root)
map_canvas.pack()

# Label to display the air quality value
air_quality_label = tk.Label(root, text="")
air_quality_label.pack()

# Button to update the air quality
update_button = tk.Button(root, text="Update Air Quality", command=lambda: update_air_quality(address_entry, map_canvas, air_quality_label))
update_button.pack()

root.mainloop()
