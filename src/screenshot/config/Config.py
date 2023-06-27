import os
import tempfile
from functools import cached_property

from utils import TIMEZONE_OFFSET, Log, Time, TimeFormat

from screenshot.config import config_utils

log = Log(__name__)


MAX_TWEET_LENGTH = 280 - 20
DIR_TEMP = os.path.join(tempfile.gettempdir(), 'tmp.screenshot')
TIME_FORMAT = TimeFormat(
    '%Y-%m-%d (%a) %I:%M%p', timezone_offset=TIMEZONE_OFFSET.LK
)


def get_timestamp():
    return TIME_FORMAT.stringify(Time.now())


class Config:
    def __init__(self, id, description, url, frequency):
        self.id = id
        self.description = description
        self.url = url
        self.frequency = frequency
        self.current_url = url

    def __str__(self):
        class_name = self.__class__.__name__
        return f'{class_name}({self.id})'

    def __repr__(self):
        return str(self)

    def download_image(self):
        raise NotImplementedError

    @cached_property
    def image_path(self):
        assert os.path.exists(DIR_TEMP)
        dir_config = os.path.join(DIR_TEMP, self.id)
        if not os.path.exists(dir_config):
            os.mkdir(dir_config)
            log.debug('Created directory ' + dir_config)
        time_id = config_utils.get_time_id_hour()
        return os.path.join(dir_config, f'{self.id}.{time_id}.png')

    @cached_property
    def tweet_text(self):
        tweet_text = f'''
{self.description}

#SriLanka #LKA #LK 🇱🇰
{get_timestamp()}
{self.current_url}
        '''.strip()
        return tweet_text
