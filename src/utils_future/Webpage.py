import os
import tempfile
import time
from functools import cached_property

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from utils import Log, hashx

from utils_future.Image import Image
from utils_future.SystemMode import SystemMode

log = Log(__name__)

T_WAIT_FOR_SCREENSHOT = 1 if SystemMode.is_test() else 240
log.debug(f'{T_WAIT_FOR_SCREENSHOT=}')


class Webpage:
    def __init__(self, url: str):
        assert url.startswith('http')
        self.url = url
        self.driver = None

        self.width, self.height = 1920, 1920
        if 'nuuuwan.github.io' in url or 'www.cricketworldcup.com' in url:
            self.width, self.height = 640, 1920
        elif 'ourworldindata.org' in url:
            self.width, self.height = 960, 960
        elif 'globalpetrolprices' in url:
            self.width, self.height = 800, 4200
        elif 'www.google.com/maps' in url:
            self.width, self.height = 1200, 675
        elif 'nuuuwan/lk_food' in url:
            self.width, self.height = 800, 4000

        self.current_url = self.url

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
        self.current_url = self.driver.current_url
        self.driver.close()
        self.driver.quit()
        log.debug(f'Closed {self.url}')

    def __screenshot_nocache__(self, elem_info):
        self.open()
        log.debug(f'😴 Sleeping for {T_WAIT_FOR_SCREENSHOT}s...')
        time.sleep(T_WAIT_FOR_SCREENSHOT)

        if not elem_info:
            self.driver.save_screenshot(self.screenshot_image_path)
        else:
            by, value = elem_info
            elem = self.find_element(by, value)
            assert elem is not None

            # HACK for CEB
            if 'cebcare.ceb.lk' in self.url:
                cur_elem = elem
                while True:
                    print(cur_elem)
                    if cur_elem.get_attribute('id') == 'panel-1':
                        break
                    cur_elem = cur_elem.find_element(By.XPATH, '..')
                if cur_elem:
                    elem = cur_elem

            elem.screenshot(self.screenshot_image_path)
        log.debug(
            f'Saved screenshot of {self.url} to {self.screenshot_image_path}'
        )
        self.close()
        return Image.load(self.screenshot_image_path)

    def screenshot(self, elem_info=None):
        if os.path.exists(self.screenshot_image_path):
            log.warn(f'{self.screenshot_image_path} exists ({self.url}).')
            return Image.load(self.screenshot_image_path)

        return self.__screenshot_nocache__(elem_info)
