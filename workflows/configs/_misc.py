from utils import TimeUnit

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
            TimeUnit.SECOND_IN.WEEK,
            Point2D(15, 120),
            Size2D(950, 700),
        ),
        ConfigScreenshot(
            'prisons_lk.statistics',
            'Statistics by Dept. of #Prisons',
            'http://prisons.gov.lk/web/en/statistics-information-en/',
            TimeUnit.SECOND_IN.WEEK,
            Point2D(360, 360),
            Size2D16x9(840),
        ),
    ]


'''
    ConfigScreenshot(
        '',
        '',
        '',
        TimeUnit.SECOND_IN.DAY,
        Point2D(1920- 1920, 1920- 1920),
        Size2D(1920, 1920),
    ),
'''
