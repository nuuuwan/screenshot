import os
import tempfile
import unittest

from screenshot import Webpage

TEST_URL = 'https://www.cbsl.gov.lk/en/sri-lanka-economy-snapshot'


class TestCase(unittest.TestCase):
    def test_get_screenshot(self):
        w = Webpage(TEST_URL)
        image_path = tempfile.mktemp(suffix='.png')
        w.get_screenshot(image_path)
        os.startfile(image_path)
