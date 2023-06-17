import os
import unittest

from screenshot import Point2D, Size2D, Webpage

DIR_TEST_OUTPUT = os.path.join('tests', 'output')


class TestCase(unittest.TestCase):
    def test_cbsl_snapshot(self):
        img = Webpage(
            'https://www.cbsl.gov.lk/en/sri-lanka-economy-snapshot'
        ).screenshot()

        left, top = 413, 493
        square_width, square_height = 240, 240
        padding = 40
        dim = 3
        square_width * dim + padding * (dim - 1)
        square_height * dim + padding * (dim - 1)

        img.crop(
            Point2D(left, top),
            Size2D(square_width, square_height),
            os.path.join(DIR_TEST_OUTPUT, 'test_cbsl_snapshot.inflation.png'),
        )
