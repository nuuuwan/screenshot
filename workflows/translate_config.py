import re

from utils import Log

from utils_future import EnglishToSinhala  # , EnglishToTamil
from workflows.CONFIG_LIST import CONFIG_LIST

log = Log(__name__)


def clean(x: str):
    x = x.replace('#', ' ')
    x = x.replace('@', ' ')
    x = re.sub(r'\s+', ' ', x)
    return x.strip()


def main():
    en_to_si = EnglishToSinhala()
    # en_to_ta = EnglishToTamil()
    for config in CONFIG_LIST:
        description = clean(config.description)

        log.info(description)
        description_si = en_to_si.translate(description)
        log.debug(description_si)
        # description_ta = en_to_ta.translate(description)
        # log.debug(description_ta)
        log.debug('-' * 8)


if __name__ == '__main__':
    main()
