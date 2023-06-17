from utils import SECONDS_IN

from screenshot import ConfigScreenshot, ConfigTE, Point2D, Size2D

CONFIG_LIST = [
    ConfigScreenshot(
        'cbsl_cpi.chart',
        'Consumer Price Inflation (#CPI) by @CBSL',
        'https://www.cbsl.gov.lk/measures-of-consumer-price-inflation',
        SECONDS_IN.AVG_MONTH,
        Point2D(380, 220),
        Size2D(780, 470),
    ),
    ConfigScreenshot(
        'cbsl_forex.chart',
        'Foreign Exchange Rates (#Forex) by @CBSL',
        'https://www.cbsl.gov.lk/rates-and-indicators/exchange-rates',
        SECONDS_IN.DAY,
        Point2D(350, 780),
        Size2D(1190, 1020),
    ),
    ConfigScreenshot(
        'dcs_snapshot.chart',
        'Economic Snapshot by @@LankaSTAT #DCS',
        'http://www.statistics.gov.lk',
        SECONDS_IN.AVG_MONTH,
        Point2D(1060, 160),
        Size2D(460, 340),
    ),
    # ConfigTE(
    #     'te.cse.stock_price',
    #     'Stock Price by @CSE_Media (via @tEconomics)',
    #     'https://tradingeconomics.com/sri-lanka/stock-market',
    # ),
    # ConfigTE(
    #     'te.cbsl.forex.usd_lkr',
    #     'LKR/USD Exchange Rage by @CBSL (via @tEconomics)',
    #     'https://tradingeconomics.com/sri-lanka/currency',
    # ),
    ConfigTE(
        'te.cbsl.gdp_annual_growth',
        '#GDP Annual Growth Rate by @CBSL (via @tEconomics)',
        'https://tradingeconomics.com/sri-lanka/gdp-growth-annual',
        SECONDS_IN.AVG_QTR,
    ),
    ConfigTE(
        'te.cbsl.forex_reserves',
        'Foreign Exchange Reserves by @CBSL (via @tEconomics)',
        'https://tradingeconomics.com/sri-lanka/foreign-exchange-reserves',
        SECONDS_IN.AVG_MONTH,
    ),
]
assert (
    len(CONFIG_LIST) <= 40
), 'CONFIG_LIST must be limited to a maximum of 40 items'
