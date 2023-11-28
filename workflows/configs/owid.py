import os
import random

from selenium.webdriver.common.by import By
from utils import SECONDS_IN, JSONFile

from screenshot import ConfigScreenshot
from screenshot.config import config_utils
from utils_future import Point2D, Size2D, Webpage

last_month = config_utils.get_last_month()

OWID_INFO_PATH = os.path.join('workflows', 'configs', 'owid_info.json')


def get_owid_url_info_list_nocache() -> list[str]:
    ROOT_URL = 'https://ourworldindata.org/country/sri-lanka'
    webpage = Webpage(ROOT_URL)
    webpage.open()
    ul_indicator = webpage.find_element(By.CLASS_NAME, 'indicators')
    url_info_list = []
    for a in ul_indicator.find_elements(By.TAG_NAME, 'a'):
        url = a.get_attribute('href')
        url = url.replace(
            'country=LKA', 'country=LKA~Southern+Asia~OWID_ASI~OWID_WRL'
        )
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
    random_i = random.randint(0, len(url_info_list) - 1)
    return url_info_list[random_i]


def get_config_list():
    owid_info = get_random_owid_url_info()
    return [
        ConfigScreenshot(
            'owid.covid.chart',
            'Daily new confirmed #COVID19 deaths'
            + ' per million people by @OurWorldInData',
            'https://ourworldindata.org'
            + '/explorers/coronavirus-data-explorer?tab=map',
            SECONDS_IN.WEEK,
            Point2D(600, 240),
            Size2D(970, 800),
        ),
        ConfigScreenshot(
            'owid.sri_lanka',
            '%s\nvia @OurWorldInData' % (owid_info['text']),
            owid_info['url'],
            SECONDS_IN.HOUR * 4,
            Point2D(1920 - 1920, 1920 - 1920),
            Size2D(1920, 1920),
            (By.CLASS_NAME, 'GrapherComponent'),
        ),
    ]
