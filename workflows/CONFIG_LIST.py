

from screenshot import Point2D, Size2D
from workflows.Config import Config

CONFIG_LIST = [
    Config(
        'cbsl_cpi.chart',
        'Consumer Price Inflation (#CPI) by @CBSL #SriLanka',
        'https://www.cbsl.gov.lk/measures-of-consumer-price-inflation',
        Point2D(380, 220),
        Size2D(780, 470),
    ),
    Config(
        'cbsl_forex.chart',
        'Foreign Exchange Rates (#Forex) by @CBSL #SriLanka',
        'https://www.cbsl.gov.lk/rates-and-indicators/exchange-rates',
        Point2D(350, 780),
        Size2D(1190, 1020),
    ),
    Config(
        'dcs_snapshot.chart',
        'Economic Snapshot by @@LankaSTAT #DCS #SriLanka',
        'http://www.statistics.gov.lk',
        Point2D(1060, 160),
        Size2D(460, 340),
    ),
]
assert (
    len(CONFIG_LIST) <= 40
), 'CONFIG_LIST must be limited to a maximum of 40 items'
