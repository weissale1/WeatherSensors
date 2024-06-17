import adafruit_dht # pip3 install adafruit-circuitpython-dht
import board
import time

from datetime import datetime
from statistics import mean

from ..domain.WeatherData import WeatherData

def load_current_weather_data():
    wd: WeatherData = _measure_weather_data()
    return wd

def _measure_weather_data():
    # get sensor data
    dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)
    raw_data = _get_sensor_data(dhtDevice, 5)
    dhtDevice.exit()

    # format and save data
    timestamp = datetime.now()
    wd: WeatherData = _format_sensor_data(timestamp, raw_data)
    return wd

def _get_sensor_data(dhtDevice, no_of_measurements_needed):
    raw_data = []
    while len(raw_data) < no_of_measurements_needed:
        try:
            temp_c = dhtDevice.temperature
            humidity = dhtDevice.humidity
            raw_data.append((temp_c, humidity))
        except RuntimeError:
            # Errors reading from DHT22 happen regularly. Simply retry.
            time.sleep(2.0)
            continue
    return raw_data

def _format_sensor_data(timestamp, raw_data) -> WeatherData:
    temps = []
    humids = []
    for d in raw_data:
        temps.append(d[0])
        humids.append(d[1])
    wd: WeatherData = WeatherData(timestamp.isoformat(timespec="seconds"), mean(temps), mean(humids))
    return wd
