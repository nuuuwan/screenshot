from selenium.webdriver.common.by import By
from utils import SECONDS_IN

from screenshot import ConfigScreenshot
from utils_future import Point2D, Size2D16x9

CONFIG_LIST_CEB = [
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
        'Present Level and Rainfall at ' + 'Major Reservoirs by @CEB_lk',
        'https://cebcare.ceb.lk/gensum/details',
        SECONDS_IN.DAY,
        Point2D(0, 0),
        Size2D16x9(1120),
        (By.ID, 'table_reservoir_rainfall_data_wrapper'),
    ),
    ConfigScreenshot(
        'ceb.power_generation.small_reservoirs',
        'Present Level and Rainfall at '
        + 'Smaller Reservoirs or Ponds by @CEB_lk',
        'https://cebcare.ceb.lk/gensum/details',
        SECONDS_IN.DAY,
        Point2D(0, 0),
        Size2D16x9(1120),
        (By.ID, 'table_pond_rainfall_data_wrapper'),
    ),
]
