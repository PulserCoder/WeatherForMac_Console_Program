from weather_api_service import Weather


def format_weather(weather: Weather) -> str:
    """Formats weather data in string"""
    return (f"{weather.city}\nTemperature: {weather.temperature}°C\n"
            f"Type of weather: {weather.weather_type.value} \n"
            f"Time of sunrise: {weather.sunrise.strftime('%H:%M')} \n"
            f"Time of sunset: {weather.sunset.strftime('%H:%M')} \n")


if __name__ == '__main__':
    from weather_api_service import get_weather
    from coordinates import get_coordinates
    print(format_weather(get_weather(get_coordinates())))