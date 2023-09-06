import random

from utils import SECONDS_IN

from screenshot import ConfigScreenshot
from screenshot.config import config_utils
from utils_future import Point2D, Size2D

last_date_id_non_weekend = config_utils.get_last_date_id_non_weekend()


CONFIG_LIST_CBSL = [
    ConfigScreenshot(
        'cbsl_cpi.chart',
        'Consumer Price Inflation (#CPI) by @CBSL',
        'https://www.cbsl.gov.lk/measures-of-consumer-price-inflation',
        SECONDS_IN.WEEK,
        Point2D(380, 220),
        Size2D(780, 470),
    ),
    ConfigScreenshot(
        'cbsl_forex.chart',
        'Foreign Exchange Rates (#Forex) by @CBSL',
        'https://www.cbsl.gov.lk/rates-and-indicators/exchange-rates',
        SECONDS_IN.DAY,
        Point2D(350, 780),
        Size2D(1190, 1020),
    ),
    ConfigScreenshot(
        'cbsl.food_prices.daily_report',
        'Daily Price Report by @CBSL #CPI #Food',
        'https://www.cbsl.gov.lk'
        + '/sites/default/files/cbslweb_documents'
        + '/statistics/pricerpt/price_report'
        + f'_{last_date_id_non_weekend}_e.pdf',
        SECONDS_IN.WEEK,
        Point2D(500, 100),
        Size2D(920, 1020),
    ),
    ConfigScreenshot(
        'cbsl.annual_report.2023.random',
        'From the 2022 Annual Report of the @CBSL',
        'https://www.cbsl.gov.lk'
        + '/sites/default/files/cbslweb_documents/publications'
        + '/AR_2022_presentation_e.pdf#page='
        + str(random.randint(6, 49)),
        SECONDS_IN.DAY,
        Point2D(160, 0),
        Size2D(1600, 933),
    ),
    ConfigScreenshot(
        'cbsl.macroeconomic_charts',
        'Macroeconomic Charts (2023 Q1) by @CBSL',
        'https://www.cbsl.gov.lk'
        + '/sites/default/files'
        + '/cbslweb_documents/statistics/mecpac'
        + '/Chart_Pack_Q1_2023_e1.pdf#page='
        + str(random.randint(4, 46)),
        SECONDS_IN.DAY,
        Point2D(1920 - 1557, 1920 - 1886),
        Size2D(1200, 900),
    ),
]
