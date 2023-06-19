import os
import time

from twtr import Tweet, Twitter
from utils import SECONDS_IN, Log

from screenshot import Config
from workflows.CONFIG_LIST import CONFIG_LIST

log = Log(__name__)

T_SLEEP_SECONDS = SECONDS_IN.MINUTE * 3
CRON_FREQUENCY = SECONDS_IN.HOUR
CRON_OVERLAP = 2


def process_config_test(config: Config):
    log.info(f'process_config_test: config={config}')

    config.download_image()
    os.startfile(config.image_path)
    log.debug(config.tweet_text)

    Tweet(config.tweet_text).add_image(config.image_path)


def process_config(config: Config, twitter: Twitter):
    if not (twitter is not None and config.should_send_tweet):
        return

    log.info(f'process_config: config={config}, {twitter=}')

    config.download_image()
    log.debug(config.tweet_text)

    tweet = Tweet(config.tweet_text).add_image(config.image_path)
    twitter.send(tweet)
    log.debug(f'😴 Sleeping for {T_SLEEP_SECONDS}s...')
    time.sleep(T_SLEEP_SECONDS)


def init_twitter():
    try:
        return Twitter()
    except Exception as e:
        log.exception(f'Failed to initialize Twitter: {e}')
        return None


def main():
    twitter = init_twitter()

    if twitter is None:
        process_config_test(CONFIG_LIST[-1])
    else:
        for config in CONFIG_LIST:
            process_config(config, twitter)


if __name__ == '__main__':
    main()
