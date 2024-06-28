from tkinter import ttk
from weather_webapi import get_temp_max_days, get_weather_info, get_days, get_recommend

def create_gui(root):
    weather_tree = ttk.Treeview(root)

    # 列の定義
    weather_tree["columns"] = ("one", "two", "three", "four", "five", "six", "seven")
    weather_tree.column("one", width=100)
    weather_tree.column("two", width=100)
    weather_tree.column("three", width=100)
    weather_tree.column("four", width=100)
    weather_tree.column("five", width=100)
    weather_tree.column("six", width=100)
    weather_tree.column("seven", width=100)

    # データの挿入
    weather_tree.insert("", 0, text="Days", values=get_days())
    weather_tree.insert("", 1, text="MaxTemps", values=get_temp_max_days())
    weather_tree.insert("", 2, text="Weather", values=get_weather_info())
    weather_tree.insert("", 3, text="Recommends", values=get_recommend())

    weather_tree.pack()
