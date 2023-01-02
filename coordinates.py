from typing import NamedTuple
from exeptions import EmptyEnv, IncorrectEnv
from config import Config


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def _coordinates_in_float(coordinates: Coordinates) -> Coordinates:
    try:
        longitude = float(coordinates.longitude)
        latitude = float(coordinates.latitude)
        return Coordinates(latitude=latitude, longitude=longitude)
    except ValueError:
        raise IncorrectEnv


def _get_coordinates_from_config() -> Coordinates:
    """Return coordinates from Config"""
    coordinates = _check_valid_coordinates(Coordinates(Config.latitude, Config.longitude))
    return _coordinates_in_float(coordinates)


def _check_valid_coordinates(coordinates: Coordinates) -> Coordinates:
    """Return coordinates and check data on valid"""
    if coordinates.longitude is None or coordinates.latitude is None:
        raise EmptyEnv
    return coordinates


def _round_coordinates() -> Coordinates:
    """Return rounded/not rounded coordinates"""
    coordinates = _get_coordinates_from_config()
    if Config.USE_ROUNDED_COORDS:
        return Coordinates(*map(lambda x: round(x, 1), [coordinates.latitude, coordinates.longitude]))
    return coordinates


def get_coordinates() -> Coordinates:
    """Return User's coordinates"""
    return _round_coordinates()


if __name__ == "__main__":
    print(get_coordinates())