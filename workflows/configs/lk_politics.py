from utils import TimeUnit

from screenshot.config import ConfigScreenshot
from utils_future import Point2D, Size2D


def get_config_list():
    return [
        ConfigScreenshot(
            "manifesto_monitoring.progress_chart",
            "\n".join(["#SriLanka #Manifesto vs. #Cabinet Decisions"]),
            "https://raw.githubusercontent.com/nuuuwan/manifesto_monitoring/refs/heads/main/images/progress_chart.png",
            TimeUnit.SECONDS_IN.WEEK * 1,
            Point2D(0, 0),
            Size2D(2400, 1350),
        ),
    ]
