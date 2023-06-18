import random

from utils import SECONDS_IN

from screenshot import ConfigScreenshot, ConfigTE, Point2D, Size2D
from screenshot.config import config_utils

date_id_non_weekend = config_utils.get_date_id_non_weekend()
last_month = config_utils.get_last_month()

CONFIG_LIST = [
    ConfigTE(
        'te.cbsl.gdp_annual_growth',
        '#GDP Annual Growth Rate by @CBSL (via @tEconomics)',
        'https://tradingeconomics.com/sri-lanka/gdp-growth-annual',
        SECONDS_IN.AVG_QTR,
    ),
    ConfigTE(
        'te.cbsl.forex_reserves',
        'Foreign Exchange Reserves by @CBSL (via @tEconomics)',
        'https://tradingeconomics.com/sri-lanka/foreign-exchange-reserves',
        SECONDS_IN.AVG_MONTH,
    ),
    ConfigScreenshot(
        'cbsl_cpi.chart',
        'Consumer Price Inflation (#CPI) by @CBSL',
        'https://www.cbsl.gov.lk/measures-of-consumer-price-inflation',
        SECONDS_IN.AVG_MONTH,
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
        'dcs_snapshot.chart',
        'Economic Snapshot by @@LankaSTAT #DCS',
        'http://www.statistics.gov.lk',
        SECONDS_IN.AVG_MONTH,
        Point2D(1060, 160),
        Size2D(460, 340),
    ),
    ConfigScreenshot(
        'moh.dengue.chart',
        '#Dengue Cases by @DengueUnit @MoH_SriLanka',
        'https://lookerstudio.google.com/reporting'
        + '/95b978f1-5c1a-44fb-a436-e19819e939c0/page/XRtTB',
        SECONDS_IN.DAY,
        Point2D(330, 70),
        Size2D(1260, 950),
    ),
    ConfigScreenshot(
        'owid.covid.chart',
        'Daily new confirmed COVID-19 deaths'
        + ' per million people by @OurWorldInData',
        'https://ourworldindata.org'
        + '/explorers/coronavirus-data-explorer?tab=map',
        SECONDS_IN.DAY,
        Point2D(600, 240),
        Size2D(970, 800),
    ),
    ConfigScreenshot(
        'ceb.power_generation.load_curve',
        'Load Curve by @CEB_lk',
        'https://cebcare.ceb.lk/gensum/details',
        SECONDS_IN.DAY,
        Point2D(800, 260),
        Size2D(1120, 720),
    ),
    ConfigScreenshot(
        'cbsl.food_prices.daily_report',
        'Daily Price Report by @CBSL #CPI #Food',
        'https://www.cbsl.gov.lk'
        + '/sites/default/files/cbslweb_documents'
        + f'/statistics/pricerpt/price_report_{date_id_non_weekend}_e.pdf',
        SECONDS_IN.DAY,
        Point2D(500, 100),
        Size2D(920, 1020),
    ),
    ConfigScreenshot(
        'cse.aspi.chart',
        '#ASPI by @CSE_Media via @FinancialTimes',
        'https://markets.ft.com/data/indices/tearsheet/summary?s=X:CSE',
        SECONDS_IN.HOUR * 6,
        Point2D(320, 900),
        Size2D(860, 520),
    ),
    ConfigScreenshot(
        'sltda.monthly_tourist_arrivals.primary_markets',
        'Top Primary Markets @SLTDA_SriLanka #Tourism',
        'https://www.sltda.gov.lk'
        + '/storage/common_media'
        + f'/MonthlyTouristArrivalsReport-{last_month}.pdf#page=6',
        SECONDS_IN.AVG_MONTH,
        Point2D(520, 220),
        Size2D(900, 1000),
    ),
    ConfigScreenshot(
        'slmetdept.temp_and_rain.last24hours',
        'Temperature & Rainfall during the last 24 hours by @SLMetDept',
        'http://www.meteo.gov.lk/index.php?lang=en',
        SECONDS_IN.HOUR * 6,
        Point2D(675, 1075),
        Size2D(300, 260),
    ),
    ConfigScreenshot(
        'cbsl.annual_report.2023.random',
        'From the 2022 Annual Report of the @CBSL',
        'https://www.cbsl.gov.lk'
        + '/sites/default/files/cbslweb_documents/publications'
        + '/AR_2022_presentation_e.pdf#page='
        + str(random.randint(6, 49)),
        SECONDS_IN.HOUR * 6,
        Point2D(160, 0),
        Size2D(1600, 933),
    ),
]
assert (
    len(CONFIG_LIST) <= 40
), 'CONFIG_LIST must be limited to a maximum of 40 items'
