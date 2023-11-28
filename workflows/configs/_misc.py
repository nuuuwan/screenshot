from utils import SECONDS_IN

from screenshot import ConfigScreenshot
from screenshot.config import config_utils
from utils_future import Point2D, Size2D, Size2D16x9

last_month = config_utils.get_last_month()


def get_config_list():
    return [
        ConfigScreenshot(
            'sltda.monthly_tourist_arrivals.primary_markets',
            '#Tourist Arrivals by Country @SLTDA_SriLanka',
            'https://www.sltda.gov.lk'
            + '/storage/common_media'
            + f'/MonthlyTouristArrivalsReport-{last_month}.pdf#page=6',
            SECONDS_IN.WEEK,
            Point2D(520, 220),
            Size2D(900, 1000),
        ),
        ConfigScreenshot(
            'lpw.property_price.chart',
            'Average #Property Prices via @LankaProperty',
            'https://www.lankapropertyweb.com/house_prices.php',
            SECONDS_IN.WEEK,
            Point2D(15, 120),
            Size2D(950, 700),
        ),
        ConfigScreenshot(
            'dwc.parktraffic',
            'National Park Visitor Service Rates'
            + ' by Dept of #Wildlife #Conservation (#DWC)',
            'http://www.dwc.gov.lk/parktraffic/graphs.php',
            SECONDS_IN.WEEK,
            Point2D(350, 0),
            Size2D(1920 - 700, 1920),
        ),
        ConfigScreenshot(
            'prisons_lk.statistics',
            'Statistics by Dept. of #Prisons',
            'http://prisons.gov.lk/web/en/statistics-information-en/',
            SECONDS_IN.WEEK,
            Point2D(360, 360),
            Size2D16x9(840),
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
