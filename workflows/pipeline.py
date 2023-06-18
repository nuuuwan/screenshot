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
    log.info(f'Processing config: {config.id}')

    config.download_image()
    log.debug(config.tweet_text)
    tweet = Tweet(config.tweet_text).add_image(config.image_path)
    if twitter is not None and config.should_send_tweet:
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
    for config in CONFIG_LIST:
        process_config(config, twitter)


if __name__ == '__main__':
    main()
