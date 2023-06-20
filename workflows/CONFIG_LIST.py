import random

from selenium.webdriver.common.by import By
from utils import SECONDS_IN

from screenshot import ConfigScreenshot, ConfigScreenshotAnimation, ConfigTE
from screenshot.config import config_utils
from screenshot.config.Ventusky import Ventusky
from utils_future import Point2D, Size2D

last_date_id_non_weekend = config_utils.get_last_date_id_non_weekend()
last_month = config_utils.get_last_month()

CONFIG_LIST = [
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
        'Economic Snapshot by @LankaSTAT #DCS',
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
        'Daily new confirmed #COVID19 deaths'
        + ' per million people by @OurWorldInData',
        'https://ourworldindata.org'
        + '/explorers/coronavirus-data-explorer?tab=map',
        SECONDS_IN.WEEK,
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
        + f'/statistics/pricerpt/price_report_{last_date_id_non_weekend}_e.pdf',
        SECONDS_IN.WEEK,
        Point2D(500, 100),
        Size2D(920, 1020),
    ),
    ConfigScreenshot(
        'sltda.monthly_tourist_arrivals.primary_markets',
        '#Tourist Arrivals by Country @SLTDA_SriLanka',
        'https://www.sltda.gov.lk'
        + '/storage/common_media'
        + f'/MonthlyTouristArrivalsReport-{last_month}.pdf#page=6',
        SECONDS_IN.AVG_MONTH,
        Point2D(520, 220),
        Size2D(900, 1000),
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
        'cse.aspi.chart',
        '#ASPI by @CSE_Media via @InvestingCom',
        'https://www.investing.com/indices/cse-all-share',
        SECONDS_IN.DAY,
        Point2D(470, 900),
        Size2D(660, 500),
    ),
    ConfigScreenshot(
        'cse.sp.charts',
        'S&P Sri Lanka 20 Index by @SPDJIndices and @CSE_Media',
        'https://www.spglobal.com'
        + '/spdji/en/exchange-relationships/exchange'
        + '/colombo-stock-exchange-cse/#overview',
        SECONDS_IN.DAY,
        Point2D(300, 710),
        Size2D(1325, 655),
    ),
    ConfigScreenshot(
        'lpw.property_price.chart',
        'Average #Property Prices via @LankaProperty',
        'https://www.lankapropertyweb.com/house_prices.php',
        SECONDS_IN.WEEK,
        Point2D(15, 120),
        Size2D(950, 700),
    ),
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
    ConfigTE(
        'te.cbsl.car_registrations',
        'Car Registrations by @CBSL (via @tEconomics)',
        'https://tradingeconomics.com/sri-lanka/car-registrations',
        SECONDS_IN.AVG_MONTH,
    ),
    ConfigTE(
        'te.cbsl.balance_of_trade',
        'Balance of #Trade by @CBSL (via @tEconomics)',
        'https://tradingeconomics.com/sri-lanka/balance-of-trade',
        SECONDS_IN.AVG_MONTH,
    ),
    ConfigTE(
        'te.cbsl.interest_date',
        '#InterestRates by @CBSL (via @tEconomics)',
        'https://tradingeconomics.com/sri-lanka/interest-rate',
        SECONDS_IN.AVG_MONTH,
    ),
    ConfigScreenshot(
        'statcounter.social_media_stats',
        '#SocialMedia Stats by @StatCounter',
        'https://gs.statcounter.com/social-media-stats/all/sri-lanka',
        SECONDS_IN.AVG_MONTH,
        Point2D(360, 125),
        Size2D(1200, 800),
    ),
    ConfigScreenshot(
        'speedtest.internet_speed',
        'Median Country #InternetSpeeds by @Speedtest',
        'https://www.speedtest.net/global-index/sri-lanka',
        SECONDS_IN.AVG_MONTH,
        Point2D(1920 - 1558, 1920 - 1691),
        Size2D(1200, 700),
    ),
    ConfigScreenshot(
        'google.maps.traffic',
        '#Traffic around #Colombo by @GoogleMaps',
        'https://www.google.com'
        + '/maps/@6.9111702,79.8750744,14z/data=!5m1!1e1?entry=ttu',
        SECONDS_IN.DAY / 4,
        Point2D(1920 - 1712, 1920 - 1645),
        Size2D(1650, 1500),
    ),
    ConfigScreenshot(
        'icc.mensodicwc2023.qualifier',
        '2023 @ICC Mens ODI @CricketWorldCup Qualifier',
        'https://www.google.com/search'
        + '?q=cricket+world+cup+qualifiers++table'
        + '&uact=5&oq=cricket+world+cup+qualifiers++table'
        + '#sie=lg;/g/11gbzbln96;5;/m/068hvv;st;fp;1;;;',
        SECONDS_IN.DAY,
        Point2D(1920 - 1335, 1920 - 1753),
        Size2D(750, 590),
    ),
    ConfigScreenshot(
        'freemeteo.temp.asia',
        'Temperature in Asia via #FreeMeteo',
        'https://freemeteo.com.lk'
        + '/weather/Sri-Lanka/maps/temperature'
        + '/?gid=9035391&country=sri-lanka',
        SECONDS_IN.HOUR * 6,
        Point2D(1920 - 1400, 1920 - 1500),
        Size2D(700, 600),
    ),
    ConfigScreenshotAnimation(
        'ventusky.temperature-2m',
        '#Temperature #Forecast (Next 24 hours) by @Ventuskycom',
        [
            Ventusky('temperature-2m').get_url_from_time(SECONDS_IN.HOUR * i)
            for i in range(0, 24, 3)
        ],
        SECONDS_IN.HOUR * 6,
        Point2D(1920 - 1920, 1920 - 1920),
        Size2D(1920, 1920),
    ),
    ConfigScreenshotAnimation(
        'ventusky.temp-feel',
        'Perceived (#FeelsLike) #Temperature #Forecast (Next 24 hours)'
        + ' by @Ventuskycom',
        [
            Ventusky('feel').get_url_from_time(SECONDS_IN.HOUR * i)
            for i in range(0, 24, 3)
        ],
        SECONDS_IN.HOUR * 6,
        Point2D(1920 - 1920, 1920 - 1920),
        Size2D(1920, 1920),
    ),
    ConfigScreenshotAnimation(
        'ventusky.rain-3h',
        '#Rainfall #Forecast (Next 24 hours) by @Ventuskycom',
        [
            Ventusky('rain-3h').get_url_from_time(SECONDS_IN.HOUR * i)
            for i in range(0, 24, 3)
        ],
        SECONDS_IN.HOUR * 6,
        Point2D(1920 - 1920, 1920 - 1920),
        Size2D(1920, 1920),
    ),
    ConfigScreenshotAnimation(
        'ventusky.humidity',
        '#RelativeHumidity (#RH) #Forecast (Next 24 hours) by @Ventuskycom',
        [
            Ventusky('humidity').get_url_from_time(SECONDS_IN.HOUR * i)
            for i in range(0, 24, 3)
        ],
        SECONDS_IN.HOUR * 6,
        Point2D(1920 - 1920, 1920 - 1920),
        Size2D(1920, 1920),
    ),
    ConfigScreenshotAnimation(
        'ventusky.aqi',
        'Air Quality (#AQI) Forecast (Next 24 hours) by @Ventuskycom',
        [
            Ventusky('aqi').get_url_from_time(SECONDS_IN.HOUR * i)
            for i in range(0, 24, 3)
        ],
        SECONDS_IN.HOUR * 6,
        Point2D(1920 - 1920, 1920 - 1920),
        Size2D(1920, 1920),
    ),
    ConfigScreenshot(
        'worldometers.population',
        'World #Population from @WorldoMeters',
        'https://www.worldometers.info/',
        SECONDS_IN.DAY,
        Point2D(0, 0),
        Size2D(440, 330),
        (By.CLASS_NAME, 'content-home'),
    ),
    ConfigScreenshot(
        'worldometers.environ_food_water',
        '#Environment, #Food and #Water from @WorldoMeters',
        'https://www.worldometers.info/',
        SECONDS_IN.DAY,
        Point2D(0, 1120),
        Size2D(440, 800),
        (By.CLASS_NAME, 'content-home'),
    ),
]
'''
Point2D(1920 - 1920, 1920- 1920),
Size2D(1920, 1920),
'''
