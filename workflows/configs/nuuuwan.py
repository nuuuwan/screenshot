from selenium.webdriver.common.by import By
from utils import SECONDS_IN

from screenshot import ConfigScreenshot
from utils_future import Point2D, Size2D16x9


def get_config_list():
    return [
        ConfigScreenshot(
            'lanka_data_search',
            '#LankaDataSearch',
            'https://nuuuwan.github.io/lanka_data_search/',
            SECONDS_IN.HOUR * 3,
            Point2D(0, 0),
            Size2D16x9(640),
            (By.ID, 'multi-line-chart'),
        ),
    ]
