import random

from utils import TimeUnit

from screenshot import ConfigScreenshot
from utils_future import Point2D, Size2D, Size2D16x9


def get_config_list():
    return [
        ConfigScreenshot(
            "dcs_snapshot.chart",
            "Economic Snapshot by @LankaSTAT #DCS",
            "http://www.statistics.gov.lk",
            TimeUnit.SECONDS_IN.WEEK,
            Point2D(1060, 160),
            Size2D(460, 340),
        ),
        ConfigScreenshot(
            "statistics.sri_lanka",
            "Statistical Pocket Book 2024\nvia @LankaSTAT",
            "https://www.statistics.gov.lk/Publication/PocketBook2024#"
            + "page=%d" % (random.randint(13, 103)),
            TimeUnit.SECONDS_IN.HOUR * 12,
            Point2D(470, 60),
            Size2D16x9(980),
        ),
    ]
