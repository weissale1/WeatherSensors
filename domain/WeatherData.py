from datetime import datetime

class WeatherData:
    def __init__(self, timestamp, temp, humid):
            self.timestamp = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S')
            self.temp = temp
            self.humid = humid

    def toJson(self) -> dict:
          return {
            'timestamp': self.timestamp.isoformat(timespec="seconds"),
            'temp': self.temp,
            'humid': self.humid
        }