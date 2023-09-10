import os
import unittest

from utils_future import Image

TEST_IMAGE_PATH = os.path.join('tests', 'image.original.png')


class TestCase(unittest.TestCase):
    def test_image_equalize_hue(self):
        im = Image.load(TEST_IMAGE_PATH)
        im.equalize_hue().write(
            TEST_IMAGE_PATH.replace('original.png', 'equalize_hue.png')
        )

    def test_image_resize(self):
        im = Image.load(TEST_IMAGE_PATH)
        im.resize(ratio=0.5).write(
            TEST_IMAGE_PATH.replace('original.png', 'resize05.png')
        )
