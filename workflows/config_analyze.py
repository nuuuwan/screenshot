import math
import statistics

from utils import SECONDS_IN, Log

from screenshot.config.Config import CRON_FREQUENCY
from workflows.CONFIG_LIST import CONFIG_LIST

log = Log(__name__)

assert (
    len(CONFIG_LIST) <= 40
), 'CONFIG_LIST must be limited to a maximum of 40 items'


def simulate():
    x = 0
    for config in CONFIG_LIST:
        config.frequency
        if config.should_send_tweet:
            x += 1
    return x


def analyze():
    N_SIMULATIONS = 10_000
    x_list = [simulate() for _ in range(N_SIMULATIONS)]
    mean = statistics.mean(x_list)
    stdev = statistics.stdev(x_list)
    CONF = 0.997
    Z = 3
    lower = mean - Z * stdev
    upper = mean + Z * stdev
    log.info(f'{mean=:.1f}, {stdev=:.1f}')
    log.info(f'{lower=:.1f} to {upper=:.1f} tweets per cron')

    PERIOD = SECONDS_IN.AVG_MONTH / CRON_FREQUENCY
    mean_period = mean * PERIOD
    stdev_period = stdev * math.sqrt(PERIOD)
    lower_period = mean_period - Z * stdev_period
    upper_period = mean_period + Z * stdev_period
    log.info(
        f'{lower_period=:.1f} to {upper_period=:.1f} tweets per {PERIOD} crons'
    )

    log.info(f'({CONF:.1%} confindence, {Z=})')


if __name__ == '__main__':
    analyze()
