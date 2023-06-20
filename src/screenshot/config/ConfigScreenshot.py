from utils import Time, TimeFormat

from screenshot.config.Config import Config
from utils_future import Webpage


def get_timestamp():
    return TimeFormat('%Y-%m-%d %H:%M').stringify(Time.now())


class ConfigScreenshot(Config):
    def __init__(
        self, id, description, url, frequency, point, size, elem_info=None
    ):
        super().__init__(id, description, url, frequency)
        self.point = point
        self.size = size
        self.elem_info = elem_info

    def download_image(self):
        img = Webpage(
            self.url,
        ).screenshot(self.elem_info)
        img.crop(
            self.point,
            self.size,
        ).write(self.image_path)
