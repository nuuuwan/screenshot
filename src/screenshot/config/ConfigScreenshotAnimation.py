import os
import tempfile
from functools import cached_property

from utils import Log

from screenshot.config.Config import Config
from screenshot.Img import Point2D, Size2D
from screenshot.Webpage import Webpage
from utils_future import AnimatedGif

log = Log(__name__)


class ConfigScreenshotAnimation(Config):
    def __init__(
        self,
        id: str,
        description: str,
        url_list: list[str],
        frequency: int,
        point: Point2D,
        size: Size2D,
    ):
        super().__init__(id, description, url_list[0], frequency)
        self.url_list = url_list
        self.point = point
        self.size = size

    @cached_property
    def image_path(self):
        parent_image_path = super().image_path
        return parent_image_path.replace('.png', '.gif')

    def download_image(self):
        image_path_list = []
        for url in self.url_list:
            image_path = tempfile.TemporaryFile(suffix='.png').name
            img = Webpage(
                url,
            ).screenshot()
            img.crop(
                self.point,
                self.size,
                image_path,
            )
            log.debug(f'Saved frame to {image_path} ')
            image_path_list.append(image_path)

        AnimatedGif(image_path_list).write(self.image_path)
        