from utils import SECONDS_IN

from screenshot.config.ConfigScreenshotAnimation import \
    ConfigScreenshotAnimation
from screenshot.config.Ventusky import Ventusky
from utils_future import Point2D, Size2D


class ConfigVentusky(ConfigScreenshotAnimation):
    def __init__(self, ventusky_id: str, title: str):
        name = f'ventusky.{ventusky_id}'
        title_final = f'{title} #Forecast (Next 24 hours) by @Ventuskycom'
        ventusky = Ventusky(ventusky_id)
        urls = [
            ventusky.get_url_from_time(SECONDS_IN.HOUR * i)
            for i in range(0, 24, 3)
        ]
        timestamps = [
            ventusky.get_timestamp(SECONDS_IN.HOUR * i)
            for i in range(0, 24, 3)
        ]
        duration = SECONDS_IN.HOUR * 12
        lefttop = Point2D(0, 0)
        size = Size2D(1920, 1920)
        super().__init__(
            name, title_final, urls, timestamps, duration, lefttop, size
        )
