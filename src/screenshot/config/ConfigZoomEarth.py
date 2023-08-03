from utils import SECONDS_IN

from screenshot.config.ConfigScreenshotAnimation import \
    ConfigScreenshotAnimation
from screenshot.config.ZoomEarth import ZoomEarth
from utils_future import Point2D, Size2D


class ConfigZoomEarth(ConfigScreenshotAnimation):
    def __init__(self, zoom_earth_id: str, title: str):
        name = f'zoom_earth.{zoom_earth_id}'
        title_final = f'{title} #Forecast (Next 24 hours) by @Zoom_Earth'
        zoom_earth = ZoomEarth(zoom_earth_id)
        urls = [
            zoom_earth.get_url_from_time(SECONDS_IN.HOUR * i)
            for i in range(0, 24, 3)
        ]
        timestamps = [
            zoom_earth.get_timestamp(SECONDS_IN.HOUR * i)
            for i in range(0, 24, 3)
        ]
        duration = SECONDS_IN.DAY
        lefttop = Point2D(0, 0)
        size = Size2D(1920, 1920)
        super().__init__(
            name, title_final, urls, timestamps, duration, lefttop, size
        )
