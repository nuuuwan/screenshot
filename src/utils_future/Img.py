from dataclasses import dataclass

from PIL import Image
from utils import Log

log = Log(__name__)


@dataclass
class Point2D:
    x: int
    y: int


@dataclass
class Size2D:
    width: int
    height: int


class Img:
    def __init__(self, image_path: str):
        self.image_path = image_path

    @property
    def im(self):
        return Image.open(self.image_path)

    def crop(
        self,
        lefttop: Point2D,
        widthheight: Size2D,
        cropped_image_path: str,
    ):
        left, top = lefttop.x, lefttop.y
        width, height = widthheight.width, widthheight.height

        bbox = (left, top, left + width, top + height)
        im_cropped = self.im.crop(bbox)
        im_cropped.save(cropped_image_path)
        log.debug(
            f'Saved cropped {self.image_path}'
            + f' ({left}, {top}) -> ({width} x {height})'
            + f' to {cropped_image_path}'
        )

    def resize(self, ratio: float, resized_image_path: str):
        im = self.im
        width, height = im.size
        newsize = (int(width * ratio), int(height * ratio))
        im_resized = im.resize(newsize)
        im_resized.save(resized_image_path)
        log.debug(
            f'Saved resized {self.image_path}'
            + f' ({width} x {height}) -> ({newsize[0]} x {newsize[1]})'
            + f' to {resized_image_path}'
        )
