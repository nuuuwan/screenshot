import time

from twtr import Tweet, Twitter
from utils import Log

from screenshot import Webpage
from workflows.Config import Config
from workflows.CONFIG_LIST import CONFIG_LIST

log = Log(__name__)

T_SLEEP_SECONDS = 30


def process_config(config: Config, twitter: Twitter):
    log.info(f'Processing config: {config.id}')
    img = Webpage(
        config.url,
    ).screenshot()

    img.crop(
        config.point,
        config.size,
        config.image_path,
    )

    log.debug(config.tweet_text)

    tweet = Tweet(config.tweet_text).add_image(config.image_path)
    if twitter is not None:
        twitter.send(tweet)
        log.debug(f'😴 Sleeping for {T_SLEEP_SECONDS}s...')
        time.sleep(T_SLEEP_SECONDS)

def main():
    try:
        twitter = Twitter()
    except Exception as e:
        log.exception(f'Failed to initialize Twitter: {e}')
        twitter = None
    for config in CONFIG_LIST:
        try:
            process_config(config, twitter)
        except Exception as e:
            log.exception(f'Failed to process config {config.id}: {e}')


if __name__ == '__main__':
    main()
