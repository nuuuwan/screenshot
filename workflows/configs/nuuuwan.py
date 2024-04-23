from selenium.webdriver.common.by import By
from utils import TimeUnit

from screenshot import ConfigScreenshot
from utils_future import Point2D, Size2D, Size2D16x9


def get_config_list():
    return [
        ConfigScreenshot(
            'lanka_data_search',
            '#LankaDataSearch',
            'https://nuuuwan.github.io/lanka_data_search/',
            TimeUnit.SECONDS_IN.HOUR * 2,
            Point2D(0, 0),
            Size2D16x9(640),
            (By.ID, 'multi-line-chart'),
        ),
        ConfigScreenshot(
            'lk_food_bpi',
            '\n'.join(
                [
                    'What is the food cost of'
                    + ' a #vegetarian packet of rice in #SriLanka?',
                    '',
                    ' #BathPacketIndex #LKFood',
                    '',
                ]
            ),
            'https://github.com/nuuuwan/lk_food/blob/main/README.md',
            TimeUnit.SECONDS_IN.HOUR * 48,
            Point2D(0, 0),
            Size2D(425, 525),
            (By.ID, 'user-content-table_bp'),
        ),
        ConfigScreenshot(
            'lk_food_protein',
            '\n'.join(
                [
                    'An adult needs ~50g of #Protein per day.',
                    '',
                    'What is the cheapest way to get 50g of'
                    + ' protein in #SriLanka?',
                    '',
                    '#LKFood',
                ]
            ),
            'https://github.com/nuuuwan/lk_food/blob/main/README.md',
            TimeUnit.SECONDS_IN.HOUR * 48,
            Point2D(0, 0),
            Size2D(550, 400),
            (By.ID, 'user-content-table_protein'),
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
            TimeUnit.SECONDS_IN.HOUR * 8,
            Point2D(0, 0),
            Size2D(1920, 1920),
            (By.ID, 'user-content-news_lk_bulletin'),
        ),
        ConfigScreenshot(
            'weather_lk_country_temperature',
            '\n'.join(
                [
                    '#Temperature by @SLMetDept',
                ]
            ),
            'https://raw.githubusercontent.com/nuuuwan/weather_lk/data/charts/country_temperature.png',
            TimeUnit.SECONDS_IN.HOUR * 8,
            Point2D(0, 700),
            Size2D(3200, 1800),
        ),
        ConfigScreenshot(
            'weather_lk_country_rainfall',
            '\n'.join(
                [
                    '#Rainfall by @SLMetDept',
                ]
            ),
            'https://raw.githubusercontent.com/nuuuwan/weather_lk/data/charts/country_rainfall.png',
            TimeUnit.SECONDS_IN.HOUR * 8,
            Point2D(0, 700),
            Size2D(3200, 1800),
        ),
        ConfigScreenshot(
            'weather_lk_colombo_temperature_91days',
            '\n'.join(
                ['#Colombo #Temperature by @SLMetDept', 'Last 91 Days']
            ),
            'https://raw.githubusercontent.com/nuuuwan/weather_lk/data/charts/temperature/79.86E-6.93N-Colombo-91days.png',
            TimeUnit.SECONDS_IN.HOUR * 16,
            Point2D(0, 700),
            Size2D(3200, 1800),
        ),
    ]
