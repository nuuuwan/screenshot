import tempfile
import unittest

from screenshot import Webpage

TEST_URL = 'https://github.com/nuuuwan/screenshot'


class TestCase(unittest.TestCase):
    def test_get_screenshot(self):
        w = Webpage(TEST_URL)
        image_path = tempfile.mktemp(suffix='.png')
        w.get_screenshot(image_path)
