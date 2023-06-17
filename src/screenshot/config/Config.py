import os
import tempfile
from functools import cached_property

from utils import Time, TimeFormat


def get_timestamp():
    return TimeFormat('%Y-%m-%d %H:%M').stringify(Time.now())


class Config:
    def __init__(self, id, description, url, frequency):
        self.id = id
        self.description = description
        self.url = url
        self.frequency = frequency

    def download_image(self):
        raise NotImplementedError

    @property
    def image_path(self):
        return os.path.join(tempfile.gettempdir(), f'{self.id}.png')

    @cached_property
    def tweet_text(self):
        return f'''
{self.description}

From {self.url}
#SriLanka 🇱🇰
({get_timestamp()})
        '''.strip()
