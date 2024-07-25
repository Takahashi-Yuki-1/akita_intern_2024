from enum import Enum
from weather.jma_forecaster import JmaForecaster
from weather.local_forecaster import LocalForecaster
from weather.forecaster import WeatherForecaster


class ForecasterType(Enum):
    """
    気象予報士の種別
    """
    JMA = 1,
    LOCAL = 2,


class WeatherForecasterAgency:
    """
    気象予報士斡旋所クラス
    """
    _instance = None
    _forecaster: WeatherForecaster

    def __new__(cls, forecaster_type=None):
        """
        気象予報士斡旋所クラスのインスタンスを取得する

        初回実行時は引数で気象予報士の種別を指定する (変更不可. 2回目の呼び出し以降は省略可)
        :param forecaster_type: 気象予報士の種別
        """
        if cls._instance is None:
            cls._instance = super(WeatherForecasterAgency, cls).__new__(cls)
            cls._instance._initialize(forecaster_type)
        return cls._instance

    def _initialize(self, forecaster_type):
        match forecaster_type:
            case ForecasterType.JMA:
                self._forecaster = JmaForecaster()
            case ForecasterType.LOCAL:
                self._forecaster = LocalForecaster()
            case _:
                raise ValueError('引数 forecaster_type が不正です')

    def refer(self):
        """
        気象予報士を紹介する
        :return: 気象予報士クラスのインスタンス
        :rtype: WeatherForecaster
        """
        return self._forecaster


