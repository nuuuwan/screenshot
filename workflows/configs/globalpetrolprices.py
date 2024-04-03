from utils import TimeUnit

from screenshot import ConfigScreenshot
from utils_future import Point2D, Size2D


def get_config(id: str, label: str) -> ConfigScreenshot:
    return ConfigScreenshot(
        f'globalpetrolprices.{id}',
        f'{label} by @GlobalPetrol',
        f'https://www.globalpetrolprices.com/{id}/',
        TimeUnit.SECOND_IN.DAY * 4,
        Point2D(0, 400),
        Size2D(800, 3400),
    )


def get_config_list():
    return [
        get_config('gasoline_prices', 'Global #Gasoline (#Petrol) Prices'),
        get_config('diesel_prices', 'Global #Diesel Prices'),
        get_config('lpg_prices', 'Global #LPG (#Gas) Prices'),
        get_config('electricity_prices', 'Global #Electricity Prices'),
    ]
