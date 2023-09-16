import os
import unittest

from utils_future import Image

IMAGE_ID_LIST = ['image', 'image2']
TEST_IMAGE_PATH_LIST = [
    os.path.join('tests', f'{id}.original.png') for id in IMAGE_ID_LIST
]


class TestCase(unittest.TestCase):
    def test_image_equalize_value(self):
        for test_image_path in TEST_IMAGE_PATH_LIST:
            im = Image.load(test_image_path)
            im.equalize_value().write(
                test_image_path.replace('original.png', 'equalize_value.png')
            )

    def test_image_resize(self):
        for test_image_path in TEST_IMAGE_PATH_LIST:
            im = Image.load(test_image_path)
            im.resize(ratio=0.5).write(
                test_image_path.replace('original.png', 'resize05.png')
            )
