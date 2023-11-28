from screenshot import ConfigVentusky, LocationConfig

LOCATION_CONFIG_SRI_LANKA = LocationConfig('sri_lanka', 7.87, 80.65, 7)

LOCATION_CONFIG_COLOMBO = LocationConfig('colombo', 6.93, 79.86, 11)


def get_config_list():
    return [
        # SRI_LANKA
        ConfigVentusky(
            'temperature-2m',
            '#Temperature',
            LOCATION_CONFIG_SRI_LANKA,
        ),
        # ConfigVentusky(
        #     'temp-feel',
        #     'Perceived (#FeelsLike) #Temperature',
        #     LOCATION_CONFIG_SRI_LANKA,
        # ),
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
        # ConfigVentusky(
        #     'gust',
        #     '#WindGusts',
        #     LOCATION_CONFIG_SRI_LANKA,
        # ),
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
        ConfigVentusky(
            'temperature-2m',
            '#Temperature',
            LOCATION_CONFIG_COLOMBO,
        ),
    ]
