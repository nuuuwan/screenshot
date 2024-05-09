import os
import random
import tempfile
import time

from twtr import Tweet, Twitter
from utils import File, Log, TimeUnit

from screenshot import Config
from workflows.all_configs import get_config_list

log = Log(__name__)

CONFIG_LIST = get_config_list()
DIR_TEMP = tempfile.gettempdir()
SHOULD_SEND_TWEET = True
PROD_LOG_PATH = os.path.join(DIR_TEMP, 'prod.log')


# Should be consistent with pipeline-cron.yml
CRON_FREQUENCY = TimeUnit.SECONDS_IN.MINUTE * 20
TEST_CONFIG_ID_PART = 'random_lk_maps'


def init_dir():
    if not os.path.exists(DIR_TEMP):
        os.mkdir(DIR_TEMP)
        log.info(f'Created Directory {DIR_TEMP}.')
    else:
        log.debug(f'Directory {DIR_TEMP} already exists.')


def init_twitter():
    try:
        return Twitter()
    except Exception as e:
        log.exception(f'Failed to initialize Twitter: {e}')
        return None


def get_run_config_list() -> list:
    random.seed(time.time())
    config_list = CONFIG_LIST.copy()
    random.shuffle(config_list)

    while True:
        for config in config_list:
            if not config.is_recently_downloaded():
                p = CRON_FREQUENCY / config.frequency
                if random.random() < p:
                    return [config]


def process_config(config: Config, twitter: Twitter):
    assert twitter is not None

    log.debug(f'Processing {config.id}...')
    config.download_image()
    log.debug(config.tweet_text)

    tweet = Tweet(config.tweet_text).add_image(config.image_path)
    if SHOULD_SEND_TWEET:
        tweet_id = twitter.send(tweet)
    else:
        tweet_id = 0

    if tweet_id is not None:
        log.info(f'🟢 Tweeted {config.id} ({tweet_id}).')
        return tweet_id

    raise Exception(f'🔴 Could NOT Tweet {config.id}!')


def main_test():
    log.info('Running pipeline in TEST mode.')

    log.debug(f'{TEST_CONFIG_ID_PART=}')
    config = [c for c in CONFIG_LIST if TEST_CONFIG_ID_PART in c.id][0]

    config.download_image()
    os.startfile(config.image_path)
    log.debug(config.tweet_text)
    Tweet(config.tweet_text).add_image(config.image_path)


def main_prod(twitter):
    log.info('Running pipeline in PROD mode.')
    n = len(CONFIG_LIST)
    prod_log_lines = []

    run_config_list = get_run_config_list()
    log.debug(f'{run_config_list=}')

    n_tweets = 0
    for config in run_config_list:
        tweet_id = process_config(config, twitter)
        prod_log_lines.append(f'{tweet_id}\t{config.id}')

    log.info(f'Tweeted {n_tweets}/{n} configs.')
    File(PROD_LOG_PATH).write('\n'.join(prod_log_lines))
    log.debug(f'Logged {PROD_LOG_PATH}')


def main():
    init_dir()
    twitter = init_twitter()
    if twitter is None:
        return main_test()

    return main_prod(twitter)


if __name__ == '__main__':
    main()
