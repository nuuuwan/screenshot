import os
import tempfile
import time
from functools import cached_property

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from utils import Hash, Log

from utils_future.Image import Image
from utils_future.SystemMode import SystemMode

log = Log(__name__)

T_WAIT_FOR_SCREENSHOT = 5 if SystemMode.is_test() else 240
log.debug(f'{T_WAIT_FOR_SCREENSHOT=}')


class Webpage:
    def __init__(self, url: str):
        assert url.startswith('http')
        self.url = url
        self.driver = None

        self.width, self.height = 1920, 1920

        for url_str, [width, height] in [
            ['nuuuwan.github.io', [640, 1920]],
            ['ourworldindata.org', [960, 960]],
            ['globalpetrolprices', [800, 4200]],
            ['www.google.com/maps', [1200, 675]],
            ['https://github.com/nuuuwan/news_lk_bulletin', [700, 2100]],
            ['weather_lk', [3200, 3200]],
        ]:
            if url_str in url:
                self.width, self.height = width, height

        self.current_url = self.url

    @cached_property
    def screenshot_image_path(self):
        h = Hash.md5(self.url)
        return os.path.join(
            tempfile.gettempdir(), f'webpage.screenshot.{h}.png'
        )

    def open(self):
        options = Options()
        options.add_argument('-headless')
        options.add_argument(f'--width={self.width}')
        options.add_argument(f'--height={self.height}')
        self.driver = webdriver.Firefox(options=options)


        # HACK!! For Ventusky
        if 'ventusky' in self.url:
            self.driver.get('https://www.ventusky.com/')
            self.driver.execute_script("window.localStorage.setItem('grid', '1');")
            self.driver.execute_script("window.localStorage.setItem('unitssystem', '1');")

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

        # HACK!!
        # os.startfile(self.screenshot_image_path)
        # raise Exception('HACK!!')
        self.close()
        return Image.load(self.screenshot_image_path)

    def screenshot(self, elem_info=None):
        if os.path.exists(self.screenshot_image_path):
            log.warn(f'{self.screenshot_image_path} exists ({self.url}).')
            return Image.load(self.screenshot_image_path)

        return self.__screenshot_nocache__(elem_info)
