from utils import Time, TimeFormat

from screenshot.config.Config import Config
from screenshot.Webpage import Webpage


def get_timestamp():
    return TimeFormat('%Y-%m-%d %H:%M').stringify(Time.now())


class ConfigScreenshot(Config):
    def __init__(self, id, description, url, frequency, point, size):
        super().__init__(id, description, url, frequency)
        self.point = point
        self.size = size

    def download_image(self):
        img = Webpage(
            self.url,
        ).screenshot()
        img.crop(
            self.point,
            self.size,
            self.image_path,
        )
