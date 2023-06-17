from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from utils import Log

log = Log(__name__)


class Webpage:
    def __init__(self, url: str):
        assert url.startswith('http')
        self.url = url
        self.driver = None
        self.width = 1920
        self.height = 1920

    def set_dims(self, width: int, height: int):
        self.width = width
        self.height = height

    def open(self):
        options = Options()
        options.add_argument('-headless')
        options.add_argument(f'--width={self.width}')
        options.add_argument(f'--height={self.height}')
        self.driver = webdriver.Firefox(options=options)
        self.driver.get(self.url)
        log.debug(f'Opened {self.url}')

    def close(self):
        self.driver.close()
        self.driver.quit()
        log.debug(f'Closed {self.url}')

    def get_screenshot(self, image_path: str):
        self.open()
        self.driver.save_screenshot(image_path)
        log.debug(f'Saved screenshot of {self.url} to {image_path}')
        self.close()
