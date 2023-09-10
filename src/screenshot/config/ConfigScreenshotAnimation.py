from functools import cached_property

from utils import Log

from screenshot.config.Config import Config
from utils_future import AnimatedGif, Point2D, Size2D, Webpage

log = Log(__name__)


class ConfigScreenshotAnimation(Config):
    def __init__(
        self,
        id: str,
        description: str,
        url_list: list[str],
        label_list: list[str],
        frequency: int,
        point: Point2D,
        size: Size2D,
    ):
        super().__init__(id, description, url_list[0], frequency)
        self.url_list = url_list
        self.label_list = label_list
        self.point = point
        self.size = size

    @cached_property
    def image_path(self):
        parent_image_path = super().image_path
        return parent_image_path.replace('.png', '.gif')

    def download_image(self):
        image_path_list = []
        for url, label in zip(self.url_list, self.label_list):
            img = (
                Webpage(
                    url,
                )
                .screenshot()
                .crop(
                    self.point,
                    self.size,
                )
            )
            width, _ = img.size
            lefttop = Point2D(width - 1000, 100)

            img = img.draw_text(lefttop, label)
            img = img.equalize_hue()
            img = img.resize(0.8)
            image_path_list.append(img.write_temp())

        AnimatedGif(image_path_list).write(self.image_path)
