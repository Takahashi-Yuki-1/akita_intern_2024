"""
天気予報を取得する抽象クラスの定義
"""
from abc import ABC, abstractmethod
from weather_forecast import WeatherForecast


class WeatherForecaster(ABC):
    """
    気象予報士クラス

    初期化時に天気予報を実行し、週間天気予報の情報を保持する
    """
    weather_forecasts: list[WeatherForecast]

    def __init__(self):
        self._forecast()

    def get(self):
        """
        週間天気予報の情報を取得する
        :return: 週間天気予報
        :rtype: list[WeatherForecast]
        """
        return self.weather_forecasts

    def re_forecast(self):
        """
        天気予報を実行し、情報を更新する
        """
        self._forecast()

    def _forecast(self):
        """
        天気予報を実行する
        """
        raw_data = self._observe()
        self.weather_forecasts = self._covert(raw_data)

    @abstractmethod
    def _observe(self):
        """
        天気を観測する
        :return: 天気予報の生データ
        :rtype: dict
        """
        pass

    @abstractmethod
    def _covert(self, raw_data):
        """
        天気の生データを保持する形式に変換する
        :param dict raw_data: 天気予報の生データ
        :return: 変換後の天気予報データ
        :rtype: list[WeatherForecast]
        """
        pass
