from utils import TIMEZONE_OFFSET, Time, TimeFormat

LAT, LNG = 7.87, 80.65
ZOOM = 8


class Ventusky:
    def __init__(self, data_type: str):
        self.data_type = data_type

    def get_url_from_time(self, delta_ut: int):
        ut = Time.now().ut + delta_ut
        # 20230621/0400
        time_id = TimeFormat(
            '%Y%m%d/%H00', timezone_offset=TIMEZONE_OFFSET.GMT
        ).stringify(Time(ut))
        return (
            'https://www.ventusky.com'
            + f'/?p={LAT};{LNG};{ZOOM}'
            + f'&l={self.data_type}'
            + f'&t={time_id}'
        )

    def get_timestamp(self, delta_ut: int):
        ut = Time.now().ut + delta_ut
        return TimeFormat(
            '%Y-%m-%d %H:00', timezone_offset=TIMEZONE_OFFSET.LK
        ).stringify(Time(ut))
