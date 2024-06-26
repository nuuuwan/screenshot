from utils import Time, TimeFormat, TimeUnit, TimeZoneOffset

from screenshot.config.Config import TIME_FORMAT

LAT, LNG = 7.87, 80.65
ZOOM = 9


class ZoomEarth:
    def __init__(self, data_type: str):
        self.data_type = data_type

    @staticmethod
    def get_time(delta_ut: int):
        Q = TimeUnit.SECONDS_IN.HOUR * 3
        start_ut = int(Time.now().ut / Q) * Q
        ut = start_ut + delta_ut
        return Time(ut)

    def get_url_from_time(self, delta_ut: int):
        time_id = TimeFormat('%Y-%m-%d,%H:00', TimeZoneOffset.GMT).stringify(
            ZoomEarth.get_time(delta_ut)
        )
        return (
            'https://zoom.earth/maps'
            + f'/{self.data_type}'
            + f'/#view={LAT},{LNG},{ZOOM}z'
            + f'/date={time_id},+5.5/model=icon'
        )

    def get_timestamp(self, delta_ut: int):
        return TIME_FORMAT.stringify(ZoomEarth.get_time(delta_ut))
