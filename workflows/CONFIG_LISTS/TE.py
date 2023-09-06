from utils import SECONDS_IN

from screenshot import ConfigTE
from screenshot.config import config_utils

last_date_id_non_weekend = config_utils.get_last_date_id_non_weekend()
last_month = config_utils.get_last_month()

CONFIG_LIST_TE = [
    ConfigTE(
        'gdp-growth-annual',
        '#GDP Annual Growth Rate by @CBSL (via @tEconomics)',
        SECONDS_IN.WEEK,
    ),
    ConfigTE(
        'foreign-exchange-reserves',
        'Foreign Exchange Reserves by @CBSL (via @tEconomics)',
        SECONDS_IN.WEEK,
    ),
    ConfigTE(
        'car-registrations',
        'Car Registrations by @CBSL (via @tEconomics)',
        SECONDS_IN.WEEK,
    ),
    ConfigTE(
        'balance-of-trade',
        'Balance of #Trade by @CBSL (via @tEconomics)',
        SECONDS_IN.WEEK,
    ),
    ConfigTE(
        'interest-rate',
        '#InterestRates by @CBSL (via @tEconomics)',
        SECONDS_IN.WEEK,
    ),
]
