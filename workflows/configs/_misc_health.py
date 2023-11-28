from utils import SECONDS_IN

from screenshot import ConfigScreenshot
from screenshot.config import config_utils
from utils_future import Point2D, Size2D

last_month = config_utils.get_last_month()


def get_config_list():
    return [
        ConfigScreenshot(
            'moh.dengue.chart',
            '#Dengue Cases by @DengueUnit @MoH_SriLanka',
            'https://lookerstudio.google.com/reporting'
            + '/95b978f1-5c1a-44fb-a436-e19819e939c0/page/XRtTB',
            SECONDS_IN.DAY,
            Point2D(330, 70),
            Size2D(1260, 950),
        ),
    ]
