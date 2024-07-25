
from src.weather_recommend_viewer import RecommendWeatherView
from weather_tree_view import WeatherTreeView
from weather.code import conv_weather_info
from weather.forecaster_agency import WeatherForecasterAgency, ForecasterType

def create_weather_viewer(root):
    view = RecommendWeatherView(root)

    # 天気予報の扱い
    agency = WeatherForecasterAgency(ForecasterType.LOCAL)
    forecaster = agency.refer()

    #天気情報を構築
    view.set_treeview(create_tree_view(root,forecaster))

    #メインウィンドウの作成
    view.get_treeview().pack()
    view.get_label().pack()
    view.get_button().pack()
    view.get_quit_button().pack()

def create_tree_view(root,forecaster):
    tree = WeatherTreeView(root)
    weekly_forecast = forecaster.get()

    for index,daily_forecast in enumerate(weekly_forecast):
        tree.add_weather_data(index,daily_forecast.date(),
                                conv_weather_info(daily_forecast.weather_code),
                                daily_forecast.temp_max)

    return tree.get_treeview()

