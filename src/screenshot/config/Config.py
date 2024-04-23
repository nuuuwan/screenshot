import os
import tempfile
from functools import cached_property

import requests
from utils import Log, Time, TimeFormat, TimeZoneOffset

from screenshot.config.config_utils import config_utils

log = Log(__name__)


DIR_TEMP = os.path.join(tempfile.gettempdir(), 'tmp.screenshot')
if not os.path.exists(DIR_TEMP):
    os.mkdir(DIR_TEMP)
    log.debug(f'Created directory {DIR_TEMP}')

TIME_FORMAT = TimeFormat('%Y-%m-%d (%a) %I:%M%p', TimeZoneOffset.LK)


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
    def image_file_name_only(self) -> str:
        time_id = config_utils.get_time_id_hour()
        return f'{self.id}.{time_id}.png'

    @cached_property
    def image_path(self):
        assert os.path.exists(DIR_TEMP)
        dir_config = os.path.join(DIR_TEMP, self.id)
        if not os.path.exists(dir_config):
            os.mkdir(dir_config)
            log.debug('Created directory ' + dir_config)
        return os.path.join(dir_config, self.image_file_name_only)

    @cached_property
    def remote_image_url(self):
        return (
            'https://raw.githubusercontent.com/nuuuwan/screenshot/data'
            + f'/{self.id}/{self.image_file_name_only}'
        )

    def is_recently_downloaded(self) -> bool:
        try:
            r = requests.head(self.remote_image_url)
            return r.status_code == 200
        except Exception as e:
            log.exception(f'Failed to check {self.remote_image_url}: {e}')
            return False

    @cached_property
    def tweet_text(self):
        tweet_text = f'''
{self.description}

#SriLanka #LKA #LK 🇱🇰
{get_timestamp()}
{self.current_url}
        '''.strip()
        return tweet_text
