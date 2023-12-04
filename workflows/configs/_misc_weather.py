from selenium.webdriver.common.by import By
from utils import SECONDS_IN

from screenshot import ConfigScreenshot
from utils_future import Point2D, Size2D


def get_config_list():
    return [
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
            'timeanddate.colombo.sun',
            '#Colombo #Sunrise, #Sunset, #DayLength by @TimeAndDate',
            'https://www.timeanddate.com/sun/sri-lanka/colombo',
            SECONDS_IN.DAY,
            Point2D(0, 0),
            Size2D(640, 360),
            (By.CLASS_NAME, 'bk-focus'),
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
            'aqicn.aq.lk',
            '#AirQuality by ##AQICN',
            'https://aqicn.org/city/sri-lanka',
            SECONDS_IN.HOUR * 8,
            Point2D(300, 260),
            Size2D(1920-600, 1920-1150),
        ),
    ]
