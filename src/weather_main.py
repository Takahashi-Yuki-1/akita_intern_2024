# main.py
import tkinter as tk
from weather_gui import create_gui

if __name__ == "__main__":
    root = tk.Tk()
    root.title("出社日おすすめお天気アプリ")
    create_gui(root)
    root.mainloop()

