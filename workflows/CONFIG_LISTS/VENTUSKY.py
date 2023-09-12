from screenshot import ConfigVentusky, LocationConfig


LOCATION_CONFIG_SRI_LANKA = LocationConfig(
    'sri_lanka', 7.87, 80.65, 8
)

LOCATION_CONFIG_COLOMBO = LocationConfig(
    'colombo', 6.93, 79.86, 10
)

CONFIG_LIST_VENTUSKY = [
    # SRI_LANKA
    ConfigVentusky(
        'temperature-2m',
        '#Temperature',
        LOCATION_CONFIG_SRI_LANKA,
    ),
    ConfigVentusky(
        'temp-feel',
        'Perceived (#FeelsLike) #Temperature',
        LOCATION_CONFIG_SRI_LANKA,
    ),
    ConfigVentusky(
        'rain-3h',
        '#Rainfall',
        LOCATION_CONFIG_SRI_LANKA,
    ),
    ConfigVentusky(
        'humidity',
        '#RelativeHumidity (#RH)',
        LOCATION_CONFIG_SRI_LANKA,
    ),
    ConfigVentusky(
        'gust',
        '#WindGusts',
        LOCATION_CONFIG_SRI_LANKA,
    ),
    ConfigVentusky(
        'aqi',
        'Air Quality (#AQI)',
        LOCATION_CONFIG_SRI_LANKA,
    ),
    # COLOMBO
    ConfigVentusky(
        'rain-3h',
        '#Rainfall',
        LOCATION_CONFIG_COLOMBO,
    ),
    ConfigVentusky(
        'aqi',
        'Air Quality (#AQI)',
        LOCATION_CONFIG_COLOMBO,
    ),
]
