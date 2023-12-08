import random

from utils import SECONDS_IN

from screenshot import ConfigScreenshot
from screenshot.config import config_utils
from utils_future import Point2D, Size2D

last_date_id_non_weekend = config_utils.get_last_date_id_non_weekend()


def get_config_list():
    return [
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
            'Macroeconomic Charts (2023 Q3) by @CBSL',
            'https://www.cbsl.gov.lk/sites/default/files/cbslweb_documents'+'/statistics/mecpac/Chart_Pack_Q3_2023_e.pdf#page='
            + str(random.randint(4, 46)),
            SECONDS_IN.DAY,
            Point2D(1920 - 1557, 1920 - 1886),
            Size2D(1200, 900),
        ),
        ConfigScreenshot(
            'cbsl.daily_economic_indicators_1',
            'Daily Economic Indicators (#ExchangeRates & #MoneyMarket) by @CBSL',
            f'https://www.cbsl.gov.lk/sites/default/files/daily_economic_indicators_{last_date_id_non_weekend}_e.pdf',
            SECONDS_IN.HOUR * 12,
            Point2D(460, 40),
            Size2D(1000, 730),
        ),
        ConfigScreenshot(
            'cbsl.daily_economic_indicators_2',
            'Daily Economic Indicators (#ShareMarket & #Energy) by @CBSL',
            f'https://www.cbsl.gov.lk/sites/default/files/daily_economic_indicators_{last_date_id_non_weekend}_e.pdf',
            SECONDS_IN.HOUR * 12,
            Point2D(460, 40 + 730),
            Size2D(1000, 1400 - 730),
        ),
    ]
