from tkinter import ttk


_HEADERS = ('Date', 'Weather', 'TempMax', 'Recommendation')
_COLUMNS = ('日付', '天気', '最高気温', 'おすすめ度')


class WeatherTable:
    table: ttk.Treeview

    def __init__(self, parent):
        self.table = ttk.Treeview(parent)
        self.table['columns'] = _COLUMNS
        for i in range(len(_COLUMNS)):
            self.table.heading(_COLUMNS[i], text=_HEADERS[i])

    def get_widget(self):
        return self.table

    def update(self, index, date, weather, temp_max, recommendation):
        self.table.insert('', index, values=(date, weather, temp_max, recommendation))

    def update_all(self, dates, weathers, temps_max, recommendations):
        for i in range(len(dates)):
            self.table.insert('', i,
                              values=(dates[i], weathers[i], temps_max[i], recommendations[i]))
