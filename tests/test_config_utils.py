import os
import unittest

from screenshot.config import config_utils

DIR_TEST_OUTPUT = os.path.join('tests', 'output')


class TestCase(unittest.TestCase):
    def test_get_last_date_id_non_weekend(self):
        last_date_id_non_weekend = config_utils.get_last_date_id_non_weekend()
        self.assertIsNotNone(last_date_id_non_weekend)

    def test_get_last_month(self):
        last_month = config_utils.get_last_month()
        self.assertIsNotNone(last_month)

    def test_get_random_gnd(self):
        gnd = config_utils.get_random_gnd()
        gnd_id = gnd.id
        self.assertEqual(gnd_id[:3], 'LK-')
        self.assertEqual(len(gnd_id), 10)

    def test_get_random_polygon(self):
        polygon, location = config_utils.get_random_polygon()
        self.assertIsNotNone(polygon)
        self.assertIsNotNone(location)
