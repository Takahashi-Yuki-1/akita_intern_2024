WEATHER_CODES = {
    100: '晴',
    200: '曇',
    202: '曇一時雨',
    212: '曇後一時雨',
    # 他のコードも追加してください
}

def conv_weather_info(code):
    info: str = WEATHER_CODES.get(code, "不明")

    return info
