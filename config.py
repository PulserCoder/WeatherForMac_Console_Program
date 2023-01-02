import dotenv
import os


class Config:
    dotenv.load_dotenv()
    latitude = os.environ.get('latitude')
    longitude = os.environ.get('longitude')
    OPENWEATHER_API = os.environ.get('OPENWEATHER_API')
    OPENWEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=' + OPENWEATHER_API + '&lang=en&units=metric'
    USE_ROUNDED_COORDS = False
