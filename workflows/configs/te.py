from utils import TimeUnit

from screenshot.config.ConfigImage import ConfigImage


def get_config(te_id: str, description: str) -> ConfigImage:
    elem_img_id = 'ImageChart'
    id = f'te.{te_id}'
    url = f'https://tradingeconomics.com/sri-lanka/{te_id}'

    return ConfigImage(
        id,
        f'{description} by @CBSL (via @tEconomics)',
        url,
        TimeUnit.SECONDS_IN.WEEK,
        elem_img_id,
    )


def get_config_list():
    return [
        get_config(
            'gdp-growth-annual',
            '#GDP Annual Growth Rate',
        ),
        get_config(
            'foreign-exchange-reserves',
            'Foreign Exchange Reserves',
        ),
        get_config(
            'car-registrations',
            'Car Registrations',
        ),
        get_config(
            'balance-of-trade',
            'Balance of #Trade',
        ),
        get_config(
            'interest-rate',
            '#InterestRates',
        ),
    ]
