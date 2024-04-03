from utils import TimeUnit

from screenshot import ConfigScreenshot
from utils_future import Point2D, Size2D


def get_config_list():
    return [
        ConfigScreenshot(
            'moh.dengue.chart',
            '#Dengue Cases by @DengueUnit @MoH_SriLanka',
            'https://lookerstudio.google.com/reporting'
            + '/95b978f1-5c1a-44fb-a436-e19819e939c0/page/XRtTB',
            TimeUnit.SECOND_IN.DAY,
            Point2D(330, 70),
            Size2D(1260, 950),
        ),
    ]
