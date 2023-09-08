import os
import unittest

from utils_future import Image

TEST_IMAGE1_PATH = os.path.join('tests', 'image1.png')
TEST_IMAGE2_PATH = os.path.join('tests', 'image2.png')


class TestCase(unittest.TestCase):
    def test_image_equalize_hue(self):
        im = Image.load(TEST_IMAGE1_PATH)
        im.equalize_hue().write(TEST_IMAGE2_PATH)
