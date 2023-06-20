import os
import random
import time

from twtr import Tweet, Twitter
from utils import SECONDS_IN, File, Log

from screenshot import DIR_TEMP, Config
from workflows.CONFIG_LIST import CONFIG_LIST

log = Log(__name__)

T_SLEEP_SECONDS_MIN = SECONDS_IN.MINUTE * 1
T_SLEEP_SECONDS_MAX = SECONDS_IN.MINUTE * 3
SHOULD_SEND_TWEET = True
PROD_LOG_PATH = os.path.join(DIR_TEMP, 'prod.log')
MAX_TWEETS_PER_CRON = 2


def random_sleep():
    t_sleep_seconds = random.uniform(T_SLEEP_SECONDS_MIN, T_SLEEP_SECONDS_MAX)
    log.debug(f'😴 Sleeping for {t_sleep_seconds}s...')
    time.sleep(t_sleep_seconds)


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


def process_config(config: Config, twitter: Twitter):
    assert twitter is not None

    if not (config.should_send_tweet):
        log.debug(f'🟠Skipping {config.id}.')
        return None

    log.debug(f'Processing {config.id}...')
    config.download_image()
    log.debug(config.tweet_text)

    tweet = Tweet(config.tweet_text).add_image(config.image_path)
    if SHOULD_SEND_TWEET:
        tweet_id = twitter.send(tweet)
    else:
        tweet_id = 0

    if tweet_id is not None:
        log.info(f'🟢Tweeted {config.id} ({tweet_id}).')
        return tweet_id

    raise Exception(f'🔴Could NOT Tweet {config.id}!')


def main_test():
    log.info('Running pipeline in TEST mode.')
    config = CONFIG_LIST[-1]
    config.download_image()
    os.startfile(config.image_path)
    log.debug(config.tweet_text)
    Tweet(config.tweet_text).add_image(config.image_path)


def main_prod(twitter):
    log.info('Running pipeline in PROD mode.')
    n = len(CONFIG_LIST)
    prod_log_lines = []

    shuffled_config_list = CONFIG_LIST
    random.shuffle(shuffled_config_list)

    n_tweets = 0
    for i, config in enumerate(shuffled_config_list):
        tweet_id = process_config(config, twitter)
        if tweet_id is not None:
            n_tweets += 1

        prod_log_lines.append(f'{tweet_id}\t{config.id}')

        if n_tweets >= MAX_TWEETS_PER_CRON:
            break

        if tweet_id is not None and i != n - 1:
            random_sleep()

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
