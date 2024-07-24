"""
天気予報をパースするためのデータクラス定義
"""
import dataclasses
import datetime
from weekday import WEEKDAYS


_DATETIME_FORMAT_BEFORE = "%Y-%m-%dT%H:%M:%S+09:00"
_DATETIME_FORMAT_AFTER = "%m/%d"
_DATE_FORMAT = "{}({})"


def _convert_date_format(date_before):
    """
    特定フォーマットの日付文字列を本プログラムで扱う日付形式に変換する
    :param date_before: 変換前の日付文字列 (ex. 2024-09-02T04:00:00+09:00 )
    :return: 変換後の日付文字列 (ex. 09/02(月) )
    """
    dt = datetime.datetime.strptime(date_before, _DATETIME_FORMAT_BEFORE)
    weekday = WEEKDAYS.get(dt.weekday(), "-")
    return _DATE_FORMAT.format(dt.strftime(_DATETIME_FORMAT_AFTER), weekday)


@dataclasses.dataclass
class WeatherForecast:
    _date_raw: str      # 生データの日付
    # date: str           # 日付 [月/日(曜日)]
    weather_code: int   # 天気コード
    pop: int            # 降水確率
    temp_max: int       # 最高気温
    temp_min: int       # 最低気温

    def __init__(self, date_raw, code, pop_raw, temp_max_raw, temp_min_raw):
        """
        1日単位の天気予報情報を生成する
        :param str date_raw: 日付文字列
        :param str code: 天気コード
        :param str pop_raw: 降水確率
        :param str temp_max_raw: 最高気温
        :param str temp_min_raw: 最低気温
        """
        # 簡略化した日付フォーマットに変換して保持する
        # self.date = _convert_date_format(date_raw)
        self._date_raw = date_raw
        # 以下、strをintに変換して保持する
        self.weather_code = int(code or -1)
        self.pop = int(pop_raw or -1)
        self.temp_max = int(temp_max_raw or -1)
        self.temp_min = int(temp_min_raw or -1)

    def date(self):
        """
        シンプルな日付文字列を取得する
        :return: 日付文字列 (ex. 07/23(火))
        :rtype: str
        """
        return _convert_date_format(self._date_raw)

    def weekday(self):
        """
        曜日コードを取得する
        :return: 曜日コード (月=0, 火=1, ..., 日=6)
        :rtype: int
        """
        return datetime.datetime.strptime(self._date_raw, _DATETIME_FORMAT_BEFORE).weekday()
