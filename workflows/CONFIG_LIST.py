import random

from selenium.webdriver.common.by import By
from utils import SECONDS_IN

from screenshot import ConfigScreenshot, ConfigTE, ConfigVentusky
from screenshot.config import config_utils
from utils_future import Point2D, Size2D, Size2D16x9

last_date_id_non_weekend = config_utils.get_last_date_id_non_weekend()
last_month = config_utils.get_last_month()

CONFIG_LIST = [
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
        'dcs_snapshot.chart',
        'Economic Snapshot by @LankaSTAT #DCS',
        'http://www.statistics.gov.lk',
        SECONDS_IN.WEEK,
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
        SECONDS_IN.WEEK,
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
        'lpw.property_price.chart',
        'Average #Property Prices via @LankaProperty',
        'https://www.lankapropertyweb.com/house_prices.php',
        SECONDS_IN.WEEK,
        Point2D(15, 120),
        Size2D(950, 700),
    ),
    ConfigTE(
        'gdp-growth-annual',
        '#GDP Annual Growth Rate by @CBSL (via @tEconomics)',
        SECONDS_IN.WEEK,
    ),
    ConfigTE(
        'foreign-exchange-reserves',
        'Foreign Exchange Reserves by @CBSL (via @tEconomics)',
        SECONDS_IN.WEEK,
    ),
    ConfigTE(
        'car-registrations',
        'Car Registrations by @CBSL (via @tEconomics)',
        SECONDS_IN.WEEK,
    ),
    ConfigTE(
        'balance-of-trade',
        'Balance of #Trade by @CBSL (via @tEconomics)',
        SECONDS_IN.WEEK,
    ),
    ConfigTE(
        'interest-rate',
        '#InterestRates by @CBSL (via @tEconomics)',
        SECONDS_IN.WEEK,
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
        SECONDS_IN.DAY,
        Point2D(1920 - 1712, 1920 - 1645),
        Size2D(1650, 1500),
    ),
    ConfigScreenshot(
        'freemeteo.temp.asia',
        'Temperature in Asia via #FreeMeteo',
        'https://freemeteo.com.lk'
        + '/weather/Sri-Lanka/maps/temperature'
        + '/?gid=9035391&country=sri-lanka',
        SECONDS_IN.WEEK,
        Point2D(1920 - 1400, 1920 - 1500),
        Size2D(700, 600),
    ),
    ConfigScreenshot(
        'worldometers.population',
        'World #Population from @WorldoMeters',
        'https://www.worldometers.info/',
        SECONDS_IN.WEEK,
        Point2D(0, 0),
        Size2D(440, 330),
        (By.CLASS_NAME, 'content-home'),
    ),
    ConfigScreenshot(
        'worldometers.environ_food_water',
        '#Environment, #Food and #Water from @WorldoMeters',
        'https://www.worldometers.info/',
        SECONDS_IN.WEEK,
        Point2D(0, 1120),
        Size2D(440, 800),
        (By.CLASS_NAME, 'content-home'),
    ),
    ConfigScreenshot(
        'heritage.economic_freedom',
        '#EconomicFreefom by @Heritage',
        'https://www.heritage.org/index/country/srilanka',
        SECONDS_IN.WEEK,
        Point2D(0, 0),
        Size2D(640, 360),
        (By.ID, 'country'),
    ),
    ConfigScreenshot(
        'timeanddate.colombo.sun',
        '#Colombo #Sunrise, #Sunset, #DayLength by @TimeAndDate',
        'https://www.timeanddate.com/sun/sri-lanka/colombo',
        SECONDS_IN.DAY,
        Point2D(0, 0),
        Size2D(640, 360),
        (By.CLASS_NAME, 'bk-focus'),
    ),
    ConfigScreenshot(
        'flightconnections.direct_flights',
        'Direct Flights to #Colombo (#CMB, #BIA) by @FlightConnec',
        'https://www.flightconnections.com/flights-to-colombo-cmb',
        SECONDS_IN.WEEK,
        Point2D(600, 600),
        Size2D(1050, 750),
    ),
    ConfigScreenshot(
        'cse.sp.charts',
        'S&P Sri Lanka 20 Index by @SPDJIndices and @CSE_Media',
        'https://www.spglobal.com'
        + '/spdji/en/exchange-relationships/exchange'
        + '/colombo-stock-exchange-cse/#overview',
        SECONDS_IN.DAY,
        Point2D(0, 0),
        Size2D(1325, 655),
        (By.CLASS_NAME, "indices-accordion-content"),
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
    ConfigScreenshot(
        'imf.lk.at_a_glance',
        'Sri Lanka "At a Glance" by @IMFNews',
        'https://www.imf.org/en/Countries/LKA#ataglance',
        SECONDS_IN.WEEK,
        Point2D(1920 - 1129, 0),
        Size2D(710, 380),
    ),
    ConfigScreenshot(
        'cselk.daily',
        '#ASPI by @CSE_Media',
        'https://cse.lk/',
        SECONDS_IN.DAY,
        Point2D(0, 0),
        Size2D(550, 380),
        (By.CLASS_NAME, 'chart-block'),
    ),
    ConfigScreenshot(
        'imf.lk.country_data',
        'Sri Lanka Country Data by @IMFNews',
        'https://www.imf.org/en/Countries/LKA#countrydata',
        SECONDS_IN.WEEK,
        Point2D(1920 - 1129, 0),
        Size2D(700, 650),
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
        'meteo_lk.weather',
        '#Weather #Forecast by @SLMetDept',
        'http://222.165.186.51/public/emfc10d.html',
        SECONDS_IN.DAY,
        Point2D(40, 40),
        Size2D(1840, 1160),
    ),
    ConfigScreenshot(
        'flightaware.bia.map',
        'Flights to and from @BIA_SriLanka by @flightaware',
        'https://flightaware.com/live/airport_status_bigmap.rvt?airport=VCBI',
        SECONDS_IN.DAY,
        Point2D(0, 0),
        Size2D(1760, 1760),
        (By.CLASS_NAME, 'ol-overlaycontainer-stopevent'),
    ),
    ConfigScreenshot(
        'lanka_data_search',
        '#LankaDataSearch',
        'https://nuuuwan.github.io/lanka_data_search/',
        SECONDS_IN.HOUR * 3,
        Point2D(0, 0),
        Size2D16x9(640),
        (By.ID, 'multi-line-chart'),
    ),
    ConfigVentusky(
        'temperature-2m',
        '#Temperature',
    ),
    ConfigVentusky(
        'temp-feel',
        'Perceived (#FeelsLike) #Temperature',
    ),
    ConfigVentusky(
        'rain-3h',
        '#Rainfall',
    ),
    ConfigVentusky(
        'humidity',
        '#RelativeHumidity (#RH)',
    ),
    ConfigVentusky(
        'gust',
        '#WindGusts',
    ),
    ConfigVentusky(
        'aqi',
        'Air Quality (#AQI)',
    ),
    ConfigScreenshot(
        'ceb.power_generation.load_curve',
        'Load Curve by @CEB_lk',
        'https://cebcare.ceb.lk/gensum/details',
        SECONDS_IN.DAY,
        Point2D(0, 0),
        Size2D16x9(1120),
        (By.ID, 'graph_load_curve'),
    ),
    ConfigScreenshot(
        'ceb.power_generation.daily_energy_share',
        'Daily Energy Share by @CEB_lk',
        'https://cebcare.ceb.lk/gensum/details',
        SECONDS_IN.DAY,
        Point2D(0, 0),
        Size2D16x9(1120),
        (By.ID, 'pie_energy_data'),
    ),
    ConfigScreenshot(
        'ceb.power_generation.major_reservoirs',
        'Present Level and Rainfall at Major Reservoirs by @CEB_lk',
        'https://cebcare.ceb.lk/gensum/details',
        SECONDS_IN.DAY,
        Point2D(0, 0),
        Size2D16x9(1120),
        (By.ID, 'table_reservoir_rainfall_data_wrapper'),
    ),
    ConfigScreenshot(
        'ceb.power_generation.small_reservoirs',
        'Present Level and Rainfall at Smaller Reservoirs or Ponds by @CEB_lk',
        'https://cebcare.ceb.lk/gensum/details',
        SECONDS_IN.DAY,
        Point2D(0, 0),
        Size2D16x9(1120),
        (By.ID, 'table_pond_rainfall_data_wrapper'),
    ),
    ConfigScreenshot(
        'asia_cup_2023.winner',
        ' #AsiaCup2023 Winning Odds by @Oddschecker',
        'https://www.oddschecker.com/cricket/asia-cup',
        SECONDS_IN.DAY,
        Point2D(0, 0),
        Size2D16x9(1120),
        (By.ID, 'outrights'),
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
