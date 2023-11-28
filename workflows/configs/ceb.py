from selenium.webdriver.common.by import By
from utils import SECONDS_IN

from screenshot import ConfigScreenshot
from utils_future import Point2D, Size2D16x9


def get_config(id: str, label: str) -> ConfigScreenshot:
    return ConfigScreenshot(
        f'ceb.power_generation.{id}',
        f'{label} by @CEB_lk',
        'https://cebcare.ceb.lk/gensum/details',
        SECONDS_IN.DAY,
        Point2D(0, 0),
        Size2D16x9(1120),
        (By.ID, id),
    )


def get_config_list():
    return [
        get_config('graph_load_curve', 'Load Curve'),
        get_config('pie_energy_data', 'Daily Energy Share'),
        get_config(
            'table_energy_data',
            'Daily Energy Data',
        ),
        get_config(
            'table_reservoir_rainfall_data_wrapper',
            'Present Level and Rainfall at ' + 'Major Reservoirs',
        ),
        get_config(
            'table_pond_rainfall_data_wrapper',
            'Present Level and Rainfall at ' + 'Smaller Reservoirs or Ponds',
        ),
    ]
