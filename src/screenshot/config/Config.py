import os
import random
import tempfile
from functools import cached_property

from utils import SECONDS_IN, Log, Time, TimeFormat

from screenshot.config import config_utils

log = Log(__name__)

# Should be consistent with pipeline-cron.yml
CRON_FREQUENCY = SECONDS_IN.HOUR
MIN_P_PROCESS = CRON_FREQUENCY / SECONDS_IN.WEEK

MAX_TWEET_LENGTH = 280 - 20
DIR_TEMP = os.path.join(tempfile.gettempdir(), 'tmp.screenshot')


def get_timestamp():
    return TimeFormat('%Y-%m-%d (%a) %I:%M%p').stringify(Time.now())


class Config:
    def __init__(self, id, description, url, frequency):
        self.id = id
        self.description = description
        self.url = url
        self.frequency = frequency

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

#SriLanka 🇱🇰

{get_timestamp()}
{self.url}

        '''.strip()
        if len(tweet_text) > MAX_TWEET_LENGTH:
            raise Exception(f'Tweet text is too long: {len(tweet_text)}')
        return tweet_text

    @property
    def should_send_tweet(self) -> bool:
        crons_per_stat = self.frequency / CRON_FREQUENCY
        p_process = max(MIN_P_PROCESS, 1.0 / crons_per_stat)

        if random.random() > p_process:
            return False
        return True
