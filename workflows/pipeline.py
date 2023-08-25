import os
import random

from twtr import Tweet, Twitter
from utils import SECONDS_IN, TIMEZONE_OFFSET, File, Log, Time, TimeFormat

from screenshot import DIR_TEMP, Config
from workflows.CONFIG_LIST import CONFIG_LIST

log = Log(__name__)

SHOULD_SEND_TWEET = True
PROD_LOG_PATH = os.path.join(DIR_TEMP, 'prod.log')

# Should be consistent with pipeline-cron.yml
CRON_FREQUENCY = SECONDS_IN.MINUTE * 20


def is_day_in_sri_lanka():
    h = int(
        TimeFormat('%H', timezone_offset=TIMEZONE_OFFSET.LK).stringify(
            Time.now()
        )
    )
    log.debug(f'{h=}')
    return 10 <= h < 22


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
    config_list = CONFIG_LIST.copy()
    random.shuffle(config_list)

    while True:
        for config in config_list:
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
    config = CONFIG_LIST[-1]
    config.download_image()
    os.startfile(config.image_path)
    log.debug(config.tweet_text)
    Tweet(config.tweet_text).add_image(config.image_path)


def main_prod(twitter):
    if not is_day_in_sri_lanka():
        log.warning('Not Daytime in Sri Lanka. Skipping.')
        return

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
