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
