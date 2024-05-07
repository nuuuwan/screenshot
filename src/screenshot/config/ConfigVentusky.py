from utils import TimeUnit

from screenshot.config.ConfigScreenshotAnimation import \
    ConfigScreenshotAnimation
from screenshot.config.LocationConfig import LocationConfig
from screenshot.config.Ventusky import Ventusky
from utils_future import Point2D, Size2D


class ConfigVentusky(ConfigScreenshotAnimation):
    def __init__(
        self, ventusky_id: str, title: str, locationConfig: LocationConfig
    ):
        location_id = locationConfig.id
        name = f'ventusky.{ventusky_id}.{location_id}'
        title_final = (
            f'{title} #Forecast (Next 48 hours)'
            + f' in #{location_id} by @Ventuskycom'
        )
        ventusky = Ventusky(ventusky_id, locationConfig)
        urls = [
            ventusky.get_url_from_time(TimeUnit.SECONDS_IN.HOUR * i)
            for i in range(0, 48, 6)
        ]
        timestamps = [
            ventusky.get_timestamp(TimeUnit.SECONDS_IN.HOUR * i)
            for i in range(0, 48, 6)
        ]
        frequency = TimeUnit.SECONDS_IN.HOUR * 8 
        lefttop = Point2D(0, 0)
        size = Size2D(1920, 1920)
        super().__init__(
            name, title_final, urls, timestamps, frequency, lefttop, size
        )
