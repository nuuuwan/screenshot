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


def process_config(config: Config, twitter: Twitter):
    log.info(f'Processing config={config.id}, {twitter=}')

    if twitter is None or config.should_send_tweet:
        config.download_image()
        log.debug(config.tweet_text)

        if twitter is None:
            os.startfile(config.image_path)

    tweet = Tweet(config.tweet_text).add_image(config.image_path)
    if twitter is not None:
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
    config_list = CONFIG_LIST
    if twitter is None:
        config_list = config_list[-1:]

    for config in config_list:
        process_config(config, twitter)


if __name__ == '__main__':
    main()
