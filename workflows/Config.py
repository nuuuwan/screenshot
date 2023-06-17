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
