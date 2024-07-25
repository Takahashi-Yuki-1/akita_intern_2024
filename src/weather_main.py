# main.py
import tkinter as tk

from src.weather_gui_manager import create_weather_viewer

if __name__ == "__main__":
    root = tk.Tk()
    create_weather_viewer(root)
    root.mainloop()
