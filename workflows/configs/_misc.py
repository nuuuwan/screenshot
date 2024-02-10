from utils import SECONDS_IN

from screenshot import ConfigScreenshot
from screenshot.config import config_utils
from utils_future import Point2D, Size2D, Size2D16x9

last_month = config_utils.get_last_month()


def get_config_list():
    return [
        ConfigScreenshot(
            'lpw.property_price.chart',
            'Average #Property Prices via @LankaProperty',
            'https://www.lankapropertyweb.com/house_prices.php',
            SECONDS_IN.WEEK,
            Point2D(15, 120),
            Size2D(950, 700),
        ),
        ConfigScreenshot(
            'prisons_lk.statistics',
            'Statistics by Dept. of #Prisons',
            'http://prisons.gov.lk/web/en/statistics-information-en/',
            SECONDS_IN.WEEK,
            Point2D(360, 360),
            Size2D16x9(840),
        ),
        ConfigScreenshot(
            'gmaps.traffic.colombo_kandy',
            '#Colombo to #Kandy #Traffic via @GoogleMaps',
            'https://www.google.com/maps/dir/Colombo/Kandy/@7.09,79.54,9z',
            SECONDS_IN.DAY,
            Point2D(1920 - 1920, 1920 - 1920),
            Size2D(1920, 1920),
        ),
        ConfigScreenshot(
            'gmaps.traffic.colombo_galle',
            '#Colombo to #Galle #Traffic via @GoogleMaps',
            'https://www.google.com/maps/dir/Colombo/Galle/@6.4870255,79.727342,9z',
            SECONDS_IN.DAY,
            Point2D(1920 - 1920, 1920 - 1920),
            Size2D(1920, 1920),
        ),
        ConfigScreenshot(
            'gmaps.traffic.all_provinces',
            'All Provincial Capitals (#TravellingSalesman) via @GoogleMaps',
            'https://www.google.com/maps/dir/Galle/Colombo/Ratnapura/Badulla/Kandy/Kurunegala/Anuradhapura/Trincomalee/Jaffna/@7.848092,79.2185451,7z',
            SECONDS_IN.DAY,
            Point2D(1920 - 1920, 1920 - 1920),
            Size2D(1920, 1920),
        ),
    ]


'''
    ConfigScreenshot(
        '',
        '',
        '',
        SECONDS_IN.DAY,
        Point2D(1920- 1920, 1920- 1920),
        Size2D(1920, 1920),
    ),
'''
