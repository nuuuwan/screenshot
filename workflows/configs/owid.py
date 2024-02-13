import os
import random
import time

from selenium.webdriver.common.by import By
from utils import SECONDS_IN, JSONFile, Log

from screenshot import ConfigScreenshot
from utils_future import Point2D, Size2D, Webpage

OWID_INFO_PATH = os.path.join('workflows', 'configs', 'owid_info.json')


log = Log('owid')
random_seed = time.time()
log.debug(f'{random_seed=}')
random.seed(random_seed)


def get_owid_url_info_list_nocache() -> list[str]:
    ROOT_URL = 'https://ourworldindata.org/country/sri-lanka'
    webpage = Webpage(ROOT_URL)
    webpage.open()
    ul_indicator = webpage.find_element(By.CLASS_NAME, 'indicators')
    url_info_list = []
    for a in ul_indicator.find_elements(By.TAG_NAME, 'a'):
        url = a.get_attribute('href')
        text = a.text
        url_info_list.append(
            dict(
                url=url,
                text=text,
            )
        )
    return url_info_list


def is_expired() -> bool:
    return random.random() < 0.01


def get_owid_url_info_list() -> list[str]:
    json_file = JSONFile(OWID_INFO_PATH)
    if not os.path.exists(OWID_INFO_PATH) or is_expired():
        url_info_list = get_owid_url_info_list_nocache()
        json_file.write(url_info_list)
    else:
        url_info_list = json_file.read()
    return url_info_list


def get_random_owid_url_info() -> str:
    url_info_list = get_owid_url_info_list()
    n = len(url_info_list)
    random_i = random.randint(0, n - 1)
    return url_info_list[random_i]


def get_config_list():
    owid_info = get_random_owid_url_info()
    text = owid_info['text']
    id = text.replace(' ', '-').replace(':', '-').lower()
    url = owid_info['url']
    url = url.replace(
        'country=LKA',
        'facet=entity&uniformYAxis=0'
        + '&time=earliest..latest'
        + '&country=LKA~IND~PAK~BGD~MYS'
        + '~Southern+Asia~South+Asia+(WB)~OWID_ASI~OWID_WRL',
    )

    return [
        ConfigScreenshot(
            f'owid.sri_lanka.{id}',
            '%s\nvia @OurWorldInData' % (text),
            url,
            SECONDS_IN.HOUR * 2,
            Point2D(1920 - 1920, 1920 - 1920),
            Size2D(1920, 1920),
            (By.CLASS_NAME, 'GrapherComponent'),
        ),
    ]
