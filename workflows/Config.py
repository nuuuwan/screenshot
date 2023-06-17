import os
import tempfile
from dataclasses import dataclass

from utils import Time, TimeFormat

from screenshot import Point2D, Size2D


def get_timestamp():
    return TimeFormat('%Y-%m-%d %H:%M').stringify(Time.now())


@dataclass
class Config:
    id: str
    description: str
    url: str
    point: Point2D
    size: Size2D

    @property
    def image_path(self):
        return os.path.join(tempfile.gettempdir(), f'{self.id}.png')

    @property
    def tweet_text(self):
        return f'''
{self.description}

From {self.url}
({get_timestamp()})
        '''.strip()



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
assert len(CONFIG_LIST) <= 40, 'CONFIG_LIST must be limited to a maximum of 40 items'