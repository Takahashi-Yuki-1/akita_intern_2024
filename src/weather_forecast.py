"""
天気予報をパースするためのデータクラス(1日単位)
"""
import dataclasses
from dataclasses import dataclass
import datetime
from weekday import WEEKDAYS


@dataclass
class WeatherForecast:
    raw_date: dataclasses.InitVar[str]  # 生データの日付
    code: dataclasses.InitVar[str]      # 天気コード
    pop: int                            # 降水確率
    temperature_max: int                # 最高気温
    temperature_min: int                # 最低気温

    date: str = dataclasses.field(init=False)       # 日付 [月/日(曜日)]
    weather: str = dataclasses.field(init=False)    # 天気（文字列）

    def __post_init__(self, raw_date: str, code: int):
        # 簡略化した日付フォーマットに変換して保持する
        self.date = _convert_date_format(raw_date)
        # 天気コードを対応した天気文字列に変換して保持する
        self.weather = _WEATHER_CODES.get(int(code), "ERROR")


_DATETIME_FORMAT_BEFORE = "%y-%m-%dT%H:%M:%S+09:00"
_DATETIME_FORMAT_AFTER = "%m/%d"
_DATE_FORMAT = "{}({})"

_WEATHER_CODES = {
    100: '晴',
    200: '曇',
    202: '曇一時雨',
    212: '曇後一時雨',
    # 他のコードも追加してください
}


def _convert_date_format(date_before):
    dt = datetime.datetime.strptime(date_before, _DATETIME_FORMAT_BEFORE)
    weekday = WEEKDAYS.get(dt.weekday(), "ERROR")
    return _DATE_FORMAT.format(dt.strftime(_DATETIME_FORMAT_AFTER), weekday)
