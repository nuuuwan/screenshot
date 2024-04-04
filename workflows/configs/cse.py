from selenium.webdriver.common.by import By
from utils import TimeUnit

from screenshot import ConfigScreenshot
from utils_future import Point2D, Size2D


def get_config_list():
    return [
        ConfigScreenshot(
            'cse.sp.charts',
            'S&P Sri Lanka 20 Index by @SPDJIndices and @CSE_Media',
            'https://www.spglobal.com'
            + '/spdji/en/exchange-relationships/exchange'
            + '/colombo-stock-exchange-cse/#overview',
            TimeUnit.SECONDS_IN.DAY,
            Point2D(0, 0),
            Size2D(1325, 655),
            (By.CLASS_NAME, "indices-accordion-content"),
        ),
        ConfigScreenshot(
            'cselk.daily',
            '#ASPI by @CSE_Media',
            'https://cse.lk/',
            TimeUnit.SECONDS_IN.DAY,
            Point2D(0, 0),
            Size2D(550, 380),
            (By.CLASS_NAME, 'chart-block'),
        ),
    ]
