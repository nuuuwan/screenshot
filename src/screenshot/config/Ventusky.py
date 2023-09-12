from utils import SECONDS_IN, TIMEZONE_OFFSET, Time, TimeFormat

from screenshot.config.Config import TIME_FORMAT
from screenshot.config.LocationConfig import LocationConfig

LAT, LNG = 7.87, 80.65
ZOOM = 8


class Ventusky:
    def __init__(self, data_type: str, locationConfig: LocationConfig):
        self.data_type = data_type
        self.locationConfig = locationConfig

    @staticmethod
    def get_time(delta_ut: int):
        Q = SECONDS_IN.HOUR * 3
        start_ut = int(Time.now().ut / Q) * Q
        ut = start_ut + delta_ut
        return Time(ut)

    def get_url_from_time(self, delta_ut: int):
        time_id = TimeFormat(
            '%Y%m%d/%H00', timezone_offset=TIMEZONE_OFFSET.GMT
        ).stringify(Ventusky.get_time(delta_ut))
        lat, lng, zoom = (
            self.locationConfig.lat,
            self.locationConfig.lng,
            self.locationConfig.zoom,
        )
        return (
            'https://www.ventusky.com'
            + f'/?p={lat};{lng};{zoom}'
            + f'&l={self.data_type}'
            + f'&t={time_id}'
        )

    def get_timestamp(self, delta_ut: int):
        return TIME_FORMAT.stringify(Ventusky.get_time(delta_ut))
