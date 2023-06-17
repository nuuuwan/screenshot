from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from utils import Log

log = Log(__name__)


class Webpage:
    def __init__(self, url: str):
        assert url.startswith('http')
        self.url = url
        self.driver = None

    def open(self):
        options = Options()
        options.add_argument('-headless')
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
