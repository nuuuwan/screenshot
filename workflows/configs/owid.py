from selenium.webdriver.common.by import By
from utils import SECONDS_IN

from screenshot import ConfigScreenshot
from screenshot.config import config_utils
from utils_future import Point2D, Size2D

last_month = config_utils.get_last_month()
owid_info = config_utils.get_random_owid_url_info()


def get_config_list():
    return [
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
            'owid.sri_lanka',
            '%s\nvia @OurWorldInData' % (owid_info['text']),
            owid_info['url'],
            SECONDS_IN.HOUR * 4,
            Point2D(1920 - 1920, 1920 - 1920),
            Size2D(1920, 1920),
            (By.CLASS_NAME, 'GrapherComponent'),
        ),
    ]
