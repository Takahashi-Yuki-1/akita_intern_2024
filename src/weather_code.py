WEATHER_CODES = {
    100: '晴',
    101: '晴時々曇',
    114: '晴後雨',
    200: '曇',
    202: '曇一時雨',
    212: '曇後一時雨',
    300: '雨',
    # 他のコードも追加してください
}


def conv_weather_info(code):
    info: str = WEATHER_CODES.get(code, "不明")

    return info
