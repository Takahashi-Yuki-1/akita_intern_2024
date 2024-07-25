"""
おすすめ度の計算に関連する関数群
"""

# 計算に用いる係数
WEATHER_COEFFICIENT = 1.2
TEMP_COEFFICIENT = 0.4
WEEKDAY_PRIORITY_COEFFICIENT = 1.4

# 天気おすすめ度の割り当て
# TODO: 割り当ては要調整
WEATHER_RECOMMENDATION_POINT_GROUP = {
    5: [100,],
    4: [101,],
    3: [200,],
    2: [114, 202, 212,],
    1: [300,],
}


def calc_recommendation(weather_code, temp_max, weekday_priority):
    """
    おすすめ度を計算する

    おすすめ度 = ( 天気おすすめ値　×　１.２ + 気温おすすめ値　×　０.４ + 曜日優先度　×　１.４ ) ÷ ３
    :param int weather_code: 天気コード
    :param int temp_max: 最高気温
    :param int weekday_priority: 曜日優先度
    :return: おすすめ度
    :rtype: float
    """
    weather_point = _get_weather_recommendation_point(weather_code) * WEATHER_COEFFICIENT
    temp_point = _get_temp_recommendation_point(temp_max) * TEMP_COEFFICIENT
    weekday_priority_point = weekday_priority * WEEKDAY_PRIORITY_COEFFICIENT

    recommendation = (weather_point + temp_point + weekday_priority_point) / 3.0

    return float('{:.1f}'.format(recommendation))


def _get_weather_recommendation_point(weather_code):
    """
    天気おすすめ値を取得する
    :param int weather_code: 天気コード
    :return: 天気おすすめ値
    :rtype: int
    """
    for key, values in WEATHER_RECOMMENDATION_POINT_GROUP.items():
        if weather_code in values:
            return key
        else:
            return 1


def _get_temp_recommendation_point(temp):
    """
    気温おすすめ値を取得する
    :param int temp: 気温
    :return: 気温おすすめ値
    :rtype: int
    """
    if temp <= 26:
        return 5
    elif 27 <= temp <= 29:
        return 4
    elif 30 <= temp <= 31:
        return 3
    elif 32 <= temp <= 34:
        return 2
    elif 35 <= temp:
        return 1


