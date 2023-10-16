import tkinter as tk
from air_quality import update_air_quality
from map_display import MapDisplay

class MainApp:
    def __init__(self, root):
        self.root = root
        root.title("Air Quality App")

        # Label and entry for the user to input city
        self.address_label = tk.Label(root, text="Enter city:")
        self.address_label.pack()

        self.address_entry = tk.Entry(root)
        self.address_entry.pack()

        # Create the map display
        self.map_display = MapDisplay(root)
        self.map_display.map_canvas.pack()

        # Label to display the air quality value
        self.air_quality_label = tk.Label(root, text="")
        self.air_quality_label.pack()

        # Button to update the air quality
        self.update_button = tk.Button(root, text="Update Air Quality", command=self.update_air_quality)
        self.update_button.pack()

    def update_air_quality(self):
        update_air_quality(self.address_entry, self.map_display, self.air_quality_label)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
