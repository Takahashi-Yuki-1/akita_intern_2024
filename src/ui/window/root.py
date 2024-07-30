import tkinter
from tkinter import ttk

from recommend.calculator import calc_recommendation
from ui.widget.setting_button import SettingButton
from ui.widget.table import WeatherTable
from weather.code import conv_weather_info
from weather.forecaster_agency import ForecasterType, WeatherForecasterAgency
from weekday_priority.manager import WeekdayPriorityManager

_WINDOW_TITLE = '出社日おすすめお天気アプリ'


class RootWindow:
    window: tkinter.Tk
    table: WeatherTable
    label: ttk.Label
    setting_button: tkinter.Button
    quit_button: tkinter.Button

    def __init__(self, forecast_type, priority_storage_type):
        self.window = tkinter.Tk()
        self.forecast_type = forecast_type
        self.priority_storage_type = priority_storage_type
        self.load()

    def load(self):
        self.window.title = _WINDOW_TITLE
        self.table = WeatherTable(self.window)
        self.label = ttk.Label(self.window)
        self.setting_button = SettingButton(self.window, callback=self._on_setting_finished())
        self.quit_button = ttk.Button(self.window, text="終了", command=self.window.quit)

        self.table.get_widget().pack()
        self.label.pack()
        self.setting_button.pack()
        self.quit_button.pack()

    def open(self):
        self.window.mainloop()

    def _on_setting_finished(self):
        forecasts = WeatherForecasterAgency().refer().get()
        priority_manager = WeekdayPriorityManager()
        for i in range(len(forecasts)):
            self.table.update(i,
                              forecasts[i].date(),
                              conv_weather_info(forecasts[i].weather_code),
                              forecasts[i].temp_max,
                              calc_recommendation(forecasts[i].weather_code,
                                                  forecasts[i].temp_max,
                                                  priority_manager.get_priority(forecasts[i].weekday())))

    @classmethod
    def builder(cls):
        """
        おすすめコメント生成のインプット要素となる優先度付きの日付クラスを作成するビルダークラスを取得する
        :return: ビルダークラス
        :rtype: PrioritizedDate.Builder
        """
        return RootWindow.Builder()

    class Builder:
        _forecast_type: int
        _priority_storage_type: int

        def forecast_type(self, forecast_type):
            self._forecast_type = forecast_type
            return self

        def priority_storage_type(self, storage_type):
            self._priority_storage_type = storage_type
            return self

        def build(self):
            if self._forecast_type is None or self._priority_storage_type is None:
                raise ValueError('必須パラメータが設定されていません')
            return RootWindow(self._forecast_type, self._priority_storage_type)
