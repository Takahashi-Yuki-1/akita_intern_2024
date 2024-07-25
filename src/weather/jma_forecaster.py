import requests

import config
from weather.forecaster import WeatherForecaster
from weather.forecast import WeatherForecast


class JmaForecaster(WeatherForecaster):
    """
    気象庁から情報を取得する気象予報士クラス
    """
    _url = 'https://www.jma.go.jp/bosai/forecast/data/forecast/050000.json'

    def _observe(self):
        return requests.get(self._url, verify=config.CERTIFICATE_ROOT).json()

    def _covert(self, raw_data):
        forecasts = []

        # 週間天気の情報を抽出する
        weekly_data = self._extract_weekly_data(raw_data)

        # 週間天気の情報から必要な情報を抽出する
        time_defines = []
        weather_codes = []
        pops = []
        temps_max = []
        temps_min = []

        # codes と pops が入ったオブジェクト、tempsMax と tempsMin が入ったオブジェクトがリストになっている
        # また、上記はオブジェクトの子要素 areas に入っている
        # 全体を回して、必要な情報を見つけたら抽出する処理にする
        for data in weekly_data:
            # 何回も見つかるが、全部同じ情報なので上書きでOK
            time_defines = data.get('timeDefines', [])
            for area in data['areas']:
                # 必要な情報があれば中身を結合、なければ空リストを結合（空なので影響なし）
                pops.extend(area.get('pops', []))
                temps_max.extend(area.get('tempsMax', []))
                temps_min.extend(area.get('tempsMin', []))
                weather_codes.extend(area.get('weatherCodes', []))

        # データクラスに変換し天気予報を保持する
        for i in range(len(time_defines)):
            forecast = WeatherForecast(time_defines[i], weather_codes[i], pops[i], temps_max[i], temps_min[i])
            forecasts.append(forecast)

        return forecasts

    @staticmethod
    def _extract_weekly_data(data):
        # 週間天気の情報(timeSeries)を抽出する
        max_length = 0
        target_data = None

        # 各要素のtimeDefinesのリスト長を比較し、最大のオブジェクトを週間天気の情報とする
        # 大元のオブジェクトが3日間の詳細予報と週間予報に分かれているため
        for report in data:
            for series in report['timeSeries']:
                length = len(series['timeDefines'])
                if length > max_length:
                    max_length = length
                    target_data = report['timeSeries']

        return target_data
