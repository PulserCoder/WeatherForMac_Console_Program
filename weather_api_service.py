from coordinates import Coordinates
import requests
from config import Config
from typing import NamedTuple
from datetime import datetime
from enum import Enum
from exeptions import ApiServiceError
from typing import Literal
from coordinates import get_coordinates

Celsius = int


class WeatherType(Enum):
    THUNDERSTORM = 'THUNDERSTORM'
    DRIZZLE = 'DRIZZLE'
    RAIN = 'RAIN'
    SNOW = 'SNOW'
    CLEAR = 'CLEAR'
    FOG = 'FOG'
    CLOUDS = 'CLOUDS'


class Weather(NamedTuple):
    temperature: Celsius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str


def _get_openweather_response(latitude: float, longitude: float) -> str:
    try:
        url = Config.OPENWEATHER_URL.format(latitude=latitude, longitude=longitude)
        return requests.get(url).json()
    except:
        raise ApiServiceError


def _parse_openweather_response(open_weather: dict) -> Weather:
    weather_type = _parse_weather_type(open_weather)
    temperature = open_weather["main"]["temp"]
    sunrise = _parse_sun_time(open_weather, 'sunrise')
    sunset = _parse_sun_time(open_weather, 'sunset')
    city = open_weather['name']
    return Weather(temperature=temperature,
                   weather_type=weather_type,
                   sunrise=sunrise,
                   sunset=sunset,
                   city=city)


def _parse_weather_type(openweather_dict: dict) -> WeatherType:
    try:
        weather_type_id = str(openweather_dict["weather"][0]["id"])
    except (IndexError, KeyError):
        raise ApiServiceError
    weather_types = {
        '1': WeatherType.THUNDERSTORM,
        '3': WeatherType.DRIZZLE,
        '5': WeatherType.RAIN,
        '7': WeatherType.SNOW,
        '800': WeatherType.CLEAR,
        '80': WeatherType.CLOUDS
    }
    for _id, _weather_type in weather_types.items():
        if weather_type_id.startswith(_id):
            return _weather_type
    raise ApiServiceError


def _parse_sun_time(openweather_dict: dict, time: Literal["sunrise"] | Literal["sunset"]) -> datetime:
    return datetime.fromtimestamp(openweather_dict["sys"][time])


def get_weather(coordinates: Coordinates) -> Weather:
    """Request weather in OpenWeather API and return result"""
    response = dict(_get_openweather_response(coordinates.latitude, coordinates.longitude))
    weather = _parse_openweather_response(response)
    return weather


if __name__ == '__main__':
    print(get_weather(get_coordinates()))
