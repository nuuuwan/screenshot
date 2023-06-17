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

    def test_cbsl_cpi(self):
        img = Webpage(
            'https://www.cbsl.gov.lk/measures-of-consumer-price-inflation'
        ).screenshot()

        img.crop(
            Point2D(380, 220),
            Size2D(780, 470),
            os.path.join(DIR_TEST_OUTPUT, 'test_cbsl_cpi.chart.png'),
        )

    def test_cbsl_forex(self):
        img = Webpage(
            'https://www.cbsl.gov.lk/rates-and-indicators/exchange-rates',
        ).screenshot()

        img.crop(
            Point2D(350, 780),
            Size2D(1190, 1020),
            os.path.join(DIR_TEST_OUTPUT, 'test_cbsl_forex.chart.png'),
        )

    def test_dcs_snapshot(self):
        img = Webpage(
            'http://www.statistics.gov.lk',
        ).screenshot()

        img.crop(
            Point2D(1060, 160),
            Size2D(460, 340),
            os.path.join(DIR_TEST_OUTPUT, 'test_dcs_snapshot.chart.png'),
        )
