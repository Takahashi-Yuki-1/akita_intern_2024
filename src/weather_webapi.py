import requests
from weather_code import conv_weather_info
import configparser


def get_weather():
    # 東京都の天気予報のURL

    config = configparser.ConfigParser()
    config.read('config.ini')

    url = config.get('DEFAULT', 'WEATHER_URL')
    certificate = config.get('DEFAULT', 'CERTIFICATE_ROOT')

    response = requests.get(url, verify=certificate)
    data = response.json()
    return data

def get_days():
    weather_data = get_weather()
    daily_days = weather_data[1]['timeSeries'][1]['timeDefines'][:7]

    return daily_days


def get_temp_max_days():
    weather_data = get_weather()
    daily_temp_max = weather_data[1]['timeSeries'][1]['areas'][0]['tempsMax'][:7]

    return daily_temp_max


def get_weather_code():
    weather_data = get_weather()
    daily_weather = weather_data[1]['timeSeries'][0]['areas'][0]['weatherCodes'][:7]

    return daily_weather


def get_recommend():
    recommend_data = []
    temps_data = get_temp_max_days()

    for temps in temps_data:
        if int(temps or 0) < 28:
            recommend_data.append("おすすめです")
        else:
            recommend_data.append("おすすめじゃないです")

    return recommend_data


def get_weather_info():
    weather_info = []
    codes = get_weather_code()

    for code in codes:
        weather_info.append(conv_weather_info(int(code)))

    return weather_info
