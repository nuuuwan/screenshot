import random

from selenium.webdriver.common.by import By
from utils import SECONDS_IN

from screenshot import ConfigScreenshot
from screenshot.config import config_utils
from utils_future import Point2D, Size2D, Size2D16x9

last_month = config_utils.get_last_month()
# polygon, location = config_utils.get_random_polygon()
owid_info = config_utils.get_random_owid_url_info()

CONFIG_LIST_MISC = [
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
        'freemeteo.temp.asia',
        'Temperature in Asia via #FreeMeteo',
        'https://freemeteo.com.lk'
        + '/weather/Sri-Lanka/maps/temperature'
        + '/?gid=9035391&country=sri-lanka',
        SECONDS_IN.WEEK,
        Point2D(1920 - 1400, 1920 - 1500),
        Size2D(700, 600),
    ),
    # ConfigScreenshot(
    #     'worldometers.population',
    #     'World #Population from @WorldoMeters',
    #     'https://www.worldometers.info/',
    #     SECONDS_IN.WEEK,
    #     Point2D(0, 0),
    #     Size2D(440, 330),
    #     (By.CLASS_NAME, 'content-home'),
    # ),
    # ConfigScreenshot(
    #     'worldometers.environ_food_water',
    #     '#Environment, #Food and #Water from @WorldoMeters',
    #     'https://www.worldometers.info/',
    #     SECONDS_IN.WEEK,
    #     Point2D(0, 1120),
    #     Size2D(440, 800),
    #     (By.CLASS_NAME, 'content-home'),
    # ),
    # ConfigScreenshot(
    #     'heritage.economic_freedom',
    #     '#EconomicFreefom by @Heritage',
    #     'https://www.heritage.org/index/country/srilanka',
    #     SECONDS_IN.WEEK,
    #     Point2D(0, 0),
    #     Size2D(640, 360),
    #     (By.ID, 'country'),
    # ),
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
        'cselk.daily',
        '#ASPI by @CSE_Media',
        'https://cse.lk/',
        SECONDS_IN.DAY,
        Point2D(0, 0),
        Size2D(550, 380),
        (By.CLASS_NAME, 'chart-block'),
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
        'lanka_data_search',
        '#LankaDataSearch',
        'https://nuuuwan.github.io/lanka_data_search/',
        SECONDS_IN.HOUR * 3,
        Point2D(0, 0),
        Size2D16x9(640),
        (By.ID, 'multi-line-chart'),
    ),
    # ConfigScreenshot(
    #     'skyfi.sri_lanka',
    #     f'{location}\nvia @SkyFiApp',
    #     'https://app.skyfi.com/explore/open?aoi=' + polygon,
    #     SECONDS_IN.HOUR * 12,
    #     Point2D(850, 550),
    #     Size2D(740, 740),
    # ),
    ConfigScreenshot(
        'owid.sri_lanka',
        '%s\nvia @OurWorldInData' % (owid_info['text']),
        owid_info['url'],
        SECONDS_IN.HOUR * 4,
        Point2D(1920 - 1920, 1920 - 1920),
        Size2D(1920, 1920),
        (By.CLASS_NAME, 'GrapherComponent'),
    ),
    ConfigScreenshot(
        'statistics.sri_lanka',
        'Statistical Pocket Book 2022\nvia @LankaSTAT',
        'http://www.statistics.gov.lk/Publication/PocketBook#'
        + 'page=%d' % (random.randint(16, 103)),
        SECONDS_IN.HOUR * 12,
        Point2D(470, 60),
        Size2D16x9(980),
    ),
    ConfigScreenshot(
        'cwc23.big_table',
        '#CWC23 Probabilities via #CWC23Simulator',
        'https://nuuuwan.github.io/cwc23/?'
        + 'context=eyJwYWdlTmFtZSI6IlByb2JhYmlsaXR5UGFnZ'
        + 'SIsInNpbXVsYXRvck1vZGVJRCI6Ik1BWElNVU1fTElLRUxJSE9PRCJ9',
        SECONDS_IN.HOUR * 8,
        Point2D(1920 - 1920, 1920 - 1920),
        Size2D(1920, 1920),
        (By.ID, 'big-table'),
    ),
    ConfigScreenshot(
        'cwc23.next_matches',
        '#CWC23 Next-Match via #CWC23Simulator',
        'https://nuuuwan.github.io/cwc23/?'
        + 'context=eyJwYWdlTmFtZSI6Ik5leHRNYXRjaGVz'
        + 'UGFnZSIsInNpbXVsYXRvck1vZGVJRCI6Ik1BWElNVU1fTElLRUxJSE9PRCJ9',
        SECONDS_IN.HOUR * 8,
        Point2D(1920 - 1920, 1920 - 1920),
        Size2D(1920, 1920),
        (By.ID, 'next-matches'),
    ),
    ConfigScreenshot(
        'cwc23.knock_out_stage',
        '#CWC23 Most Likely Scenario in Knock-Out Stage via #CWC23Simulator',
        'https://nuuuwan.github.io/cwc23/?'
        + 'context=eyJwYWdlTmFtZSI6IlNpbXVsYXRvclBhZ2UiLC'
        + 'JzaW11bGF0b3JNb2RlSUQiOiJNQVhJTVVNX0xJS0VMSUhPT0QifQ%3D%3D',
        SECONDS_IN.HOUR * 8,
        Point2D(1920 - 1920, 1920 - 1920),
        Size2D(1920, 1920),
        (By.ID, 'knock-out-stage'),
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
