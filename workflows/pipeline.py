from utils import Log

from screenshot import Webpage
from workflows.Config import Config, CONFIG_LIST
from twtr import Twitter, Tweet

log = Log(__name__)


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
    twitter.send(tweet)


def main():
    twitter = Twitter()
    for config in CONFIG_LIST:
        try:
            process_config(config, twitter)
        except Exception as e:
            log.exception(f'Failed to process config {config.id}: {e}')


if __name__ == '__main__':
    main()
