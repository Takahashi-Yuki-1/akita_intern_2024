import json
from weather_forecast import WeatherForecast
from weather_forecaster import WeatherForecaster


class LocalForecaster(WeatherForecaster):
    """
    ローカルのモックファイルから情報を取得する気象予報士クラス
    """
    _file_path = './../resource/weather_forecast_mock.json'

    def _observe(self):
        with open(self._file_path, 'r', encoding='utf-8') as raw_data:
            return json.load(raw_data)

    def _covert(self, raw_data):
        forecasts = []

        for obj in raw_data:
            forecast = WeatherForecast(obj['date'], obj['code'], obj['pop'], obj['tempMax'], obj['tempMin'])
            forecasts.append(forecast)

        return forecasts
