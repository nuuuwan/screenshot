from selenium.webdriver.common.by import By
from utils import WWW, Log

from screenshot.config.Config import Config
from screenshot.Webpage import Webpage

log = Log(__name__)


class ConfigImage(Config):
    def __init__(self, id, description, url, frequency, elem_img_id):
        super().__init__(id, description, url, frequency)
        self.elem_img_id = elem_img_id

    def download_image(self):
        webpage = Webpage(
            self.url,
        )
        webpage.open()
        img_src = webpage.find_element(By.ID, "ImageChart").get_attribute(
            'src'
        )
        webpage.close()
        log.debug(f'{img_src=}')

        WWW.download_binary(img_src, self.image_path)
        log.debug(f'Downloaded image from {img_src} to {self.image_path}')
