from __future__ import annotations

REGION_TO_COUNTRY_COORDINATE_MAPPING = {
    "hongkong": (22.2793278, 114.1628131),
    "singapore": (1.357107, 103.8194992),
    "sydney": (-33.8698439, 151.2082848),
    "japan": (36.5748441, 139.2394179),
    "southafrica": (-28.8166236, 24.991639),
    "india": (22.3511148, 78.6677428),
    "eu": (46.603354, 1.8883335),
    "amsterdam": (52.3727598, 4.8936041),
    "frankfurt": (50.1106444, 8.6820917),
    "russia": (64.6863136, 97.7453061),
    "london": (51.5073219, -0.1276474),
    "us_central": (41.7872548, -87.8410043),
    "us_west": (37.7577627, -122.4727051),
    "us_east": (40.707938, -74.0423759),
    "us_south": (32.7870795, -96.7988588),
    "brazil": (-10.3333333, -53.2),
    "rotterdam": (51.9240069, 4.4777325),
}

DEFAULT_REGIONS = list(REGION_TO_COUNTRY_COORDINATE_MAPPING.keys())
