import os
import tempfile
from functools import cached_property

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from utils import Log, hashx

from screenshot.Img import Img

log = Log(__name__)


class Webpage:
    def __init__(self, url: str):
        assert url.startswith('http')
        self.url = url
        self.driver = None
        self.width = 1920
        self.height = 1920

    @cached_property
    def screenshot_image_path(self):
        h = hashx.md5(self.url)
        return os.path.join(
            tempfile.gettempdir(), f'webpage.screenshot.{h}.png'
        )

    def open(self):
        options = Options()
        options.add_argument('-headless')
        options.add_argument(f'--width={self.width}')
        options.add_argument(f'--height={self.height}')
        self.driver = webdriver.Firefox(options=options)
        self.driver.get(self.url)
        log.debug(f'Opened {self.url}')

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def close(self):
        self.driver.close()
        self.driver.quit()
        log.debug(f'Closed {self.url}')

    def __screenshot_nocache__(self):
        self.open()
        self.driver.save_screenshot(self.screenshot_image_path)
        log.debug(
            f'Saved screenshot of {self.url} to {self.screenshot_image_path}'
        )
        self.close()
        return Img(self.screenshot_image_path)

    def screenshot(self):
        if os.path.exists(self.screenshot_image_path):
            log.warn(f'{self.screenshot_image_path} exists.')
            return Img(self.screenshot_image_path)

        return self.__screenshot_nocache__()
