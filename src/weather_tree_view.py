from tkinter import ttk

class WeatherTreeView:

    treeview: ttk.Treeview

    def __init__(self, root):
        self.treeview = ttk.Treeview(root)
        self._make_column()
        self._make_header()

    def _make_column(self):
        self.treeview["columns"] = ("Date", "Weather", "TempMax", "Recommends")  # 列の定義

    def _make_header(self):
        self.treeview.heading("Date", text="日付", anchor='w')
        self.treeview.heading("Weather", text="天気", anchor='w')
        self.treeview.heading("TempMax", text="最高気温", anchor='w')
        self.treeview.heading("Recommends", text="おすすめ度", anchor='w')

    def get_treeview(self):
        return self.treeview

    def add_weather_data(self,index,date,weather,temp_max):
        self.treeview.insert("", index, values=(date,weather,temp_max))
