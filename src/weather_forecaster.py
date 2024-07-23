"""
天気予報を取得する抽象クラス
"""
from abc import ABC, abstractmethod
from weather_forecast import WeatherForecast


class WeatherForecaster(ABC):
    weather_forecasts: list[WeatherForecast]

    def __init__(self):
        self._forecast()

    def get(self):
        return self.weather_forecasts

    def re_forecast(self):
        self._forecast()

    def _forecast(self):
        raw_data = self._observe()
        self.weather_forecasts = self._covert(raw_data)

    @abstractmethod
    def _observe(self):
        pass

    @abstractmethod
    def _covert(self, raw_data: str):
        pass
