import os
import tempfile

from PIL import Image as PILImage
from PIL import ImageDraw, ImageEnhance, ImageFont
from utils import Log

from utils_future.Point2D import Point2D
from utils_future.Size2D import Size2D

log = Log(__name__)

FONT_PATH = os.path.join('src', 'utils_future', 'CONSOLAB.TTF')
FONT = ImageFont.truetype(FONT_PATH, 60)
TEXT_COLOR = (255, 255, 255)


class Image:
    def __init__(self, im: PILImage.Image):
        self.im = im

    @staticmethod
    def load(image_path: str):  # -> Image
        return Image(PILImage.open(image_path))

    def write(self, image_path: str) -> str:
        self.im.save(image_path)
        log.debug(f'Saved {image_path}')
        return image_path

    def write_temp(self):
        return self.write(tempfile.NamedTemporaryFile(suffix='.png').name)

    @property
    def size(self):
        return self.im.size

    def crop(
        self,
        lefttop: Point2D,
        widthheight: Size2D,
    ):  # -> Image
        crop_width, crop_height = widthheight.to_tuple()
        im_width, im_height = self.im.size
        if crop_height > im_height:
            log.warning(f'crop height {crop_height} > {im_height}')
            crop_height = im_height
            
        if crop_width > im_width:
            log.warning(f'crop width {crop_width} > {im_width}')
            crop_width = im_width
            
        bbox = lefttop.to_tuple() + (lefttop + widthheight).to_tuple()
        im = self.im.crop(bbox)
        log.debug(f'Cropped image to {lefttop} and {widthheight}')
        return Image(im)

    def resize(self, ratio: float):  # -> Image
        im = self.im
        width, height = im.size
        newsize = (int(width * ratio), int(height * ratio))
        im = im.resize(newsize)
        log.debug(f'Resized image by {ratio} to size({newsize})')
        return Image(im)

    def draw_text(self, lefttop: Point2D, text: str):  # -> Image
        draw = ImageDraw.Draw(self.im)
        draw.text(lefttop.to_tuple(), text, TEXT_COLOR, font=FONT)
        log.debug(f'Drew text "{text}" at {lefttop}')
        return Image(self.im)

    @staticmethod
    def equalize_map(x_list: list[float]) -> list[float]:
        x_list_sorted = sorted(x_list)
        n = len(x_list_sorted)
        idx = {}
        for i, x in enumerate(x_list_sorted):
            p = i / n
            if x not in idx:
                idx[x] = p
        return idx

    @staticmethod
    def equalize(c):
        idx = Image.equalize_map(list(c.getdata()))
        return c.point(lambda x: int(idx.get(x, 0) * 255))

    def equalize_value(self):  # -> Image
        im = self.im.convert('HSV')
        h, s, v = im.split()
        v = Image.equalize(v)

        im = PILImage.merge('HSV', (h, s, v))
        im = im.convert('RGB')
        log.debug('Equalized hue')
        return Image(im)

    def enhance(self, factor):  # -> Image
        enhancer = ImageEnhance.Contrast(self.im)
        im2 = enhancer.enhance(factor)
        return Image(im2)
