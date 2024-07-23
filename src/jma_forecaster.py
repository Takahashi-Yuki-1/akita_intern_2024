"""
気象庁のAPIから天気予報を取得する
"""
import json
import requests
import configparser
from weather_forecaster import WeatherForecaster
from weather_forecast import WeatherForecast


class JmaForecaster(WeatherForecaster):

    def _observe(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        url = config.get('DEFAULT', 'WEATHER_URL')
        certificate = config.get('DEFAULT', 'CERTIFICATE_ROOT')

        return requests.get(url, verify=certificate)

    def _covert(self, raw_data: str):
        json_data = json.loads(raw_data)

        # 週間天気の情報を抽出する
        weekly_data = _extract_weekly_data(json_data)

        # 週間天気の情報から必要な情報を抽出する
        time_defines = []
        weather_codes = []
        pops = []
        temps_max = []
        temps_min = []

        for series in weekly_data['series']:
            time_defines = weekly_data.get('timeDefines', [])
            for area in series['areas']:
                pops = area.get('pops', [])
                temps_max = area.get('tempsMax', [])
                temps_min = area.get('tempsMin', [])
                weather_codes = area.get('weatherCodes', [])

        # データクラスに変換し天気予報を保持する
        self.weather_forecasts = []
        for i in range(len(time_defines)):
            forecast = WeatherForecast(time_defines[i], weather_codes[i], pops[i], temps_max[i], temps_min[i])
            self.weather_forecasts.append(forecast)


def _extract_weekly_data(data):
    # 週間天気の情報(timeSeries)を抽出する
    max_length = 0
    target_data = None

    for report in data:
        for series in report['timeSeries']:
            length = len(series['timeDefines'])
            if length > max_length:
                max_length = length
                target_data = report['timeSeries']

    return target_data
