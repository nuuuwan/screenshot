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
            SECONDS_IN.HOUR * 2,
            Point2D(0, 0),
            Size2D16x9(640),
            (By.ID, 'multi-line-chart'),
        ),
        ConfigScreenshot(
            'lk_food_bath_packet_index',
            '\n'.join(
                [
                    'What is the food cost of',
                    ' a vegetarian packet of rice in #SriLanka?',
                    '',
                    ' #BathPacketIndex #LKFood',
                    '',
                ]
            ),
            'https://github.com/nuuuwan/lk_food/blob/main/README.md',
            SECONDS_IN.HOUR * 24,
            Point2D(0, 0),
            Size2D16x9(640),
            (By.TAG_NAME, 'table'),
        ),
        ConfigScreenshot(
            'news_lk_bulletin',
            '\n'.join(
                [
                    '#SriLankaNewsBulletin',
                    '#SriLanka #News',
                ]
            ),
            'https://github.com/nuuuwan/news_lk_bulletin/blob/main/README.md',
            SECONDS_IN.HOUR * 4,
            Point2D(0, 0),
            Size2D16x9(1200),
            (By.ID, 'user-content-news_lk_bulletin'),
        ),
    ]
