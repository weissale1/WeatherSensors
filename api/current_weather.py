from flask import Blueprint, jsonify

from ..domain.WeatherData import WeatherData
from ..services.gather_data import load_current_weather_data

bp = Blueprint('current_weather', __name__, url_prefix='/current')

@bp.route("/", methods=['GET'], strict_slashes=False)
def index():
    return CurrentWeather.get_current_weather()

class CurrentWeather:
    def get_current_weather():
        wd: WeatherData = load_current_weather_data()
        return jsonify(wd.toJson())
 