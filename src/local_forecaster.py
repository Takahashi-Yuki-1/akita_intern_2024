"""
ローカルファイルから天気予報を取得する
"""
from weather_forecaster import WeatherForecaster


class LocalForecaster(WeatherForecaster):
    def _observe(self):
        pass

    def _covert(self, raw_data: str):
        pass
