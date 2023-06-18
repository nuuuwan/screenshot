import os
import random
import tempfile
from functools import cached_property

from utils import SECONDS_IN, Log, Time, TimeFormat

log = Log(__name__)

# Should be consistent with pipeline-cron.yml
CRON_FREQUENCY = SECONDS_IN.HOUR
CRON_OVERLAP = 2


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

    @property
    def should_send_tweet(self) -> bool:
        crons_per_stat = self.frequency / CRON_FREQUENCY
        p_process = CRON_OVERLAP * 1.0 / crons_per_stat

        log.debug(
            f'config.frequency = {self.frequency}s,'
            + f' {crons_per_stat=}, {p_process=}'
        )

        if random.random() > p_process:
            log.debug(f'Skipping {self.id}...')
            return False
        return True
