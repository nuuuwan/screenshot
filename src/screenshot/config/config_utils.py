import random

from gig import Ent, EntType
from utils import SECONDS_IN, Log, String, Time, TimeFormat

log = Log('config_utils')


def get_time_id_hour():
    ut = Time.now().ut
    return TimeFormat('%Y%m%d.%H0000').stringify(Time(ut))


def get_last_date_id_non_weekend():
    ut = Time.now().ut
    day_of_week = TimeFormat('%a').stringify(Time(ut))

    # If Sunday or Monday, get the previous Friday. Else the previous day.
    if day_of_week == 'Sun':
        ut = ut - 2 * SECONDS_IN.DAY
    elif day_of_week == 'Mon':
        ut = ut - 3 * SECONDS_IN.DAY
    else:
        ut = ut - SECONDS_IN.DAY

    return TimeFormat('%Y%m%d').stringify(Time(ut))


def get_last_month():
    ut = Time.now().ut
    ut = ut - SECONDS_IN.AVG_MONTH
    return TimeFormat('%B').stringify(Time(ut))


def get_random_gnd():
    gnd_list = Ent.list_from_type(EntType.GND)
    random_i = random.randint(0, len(gnd_list) - 1)
    return gnd_list[random_i]


def get_location(gnd):
    lat0, lng0 = gnd.centroid
    dsd = Ent.from_id(gnd.dsd_id)
    district = Ent.from_id(gnd.district_id)
    province = Ent.from_id(gnd.province_id)

    return '\n'.join(
        [
            f'#{String(gnd.name).camel} GND ({gnd.id}),',
            f'#{String(dsd.name).camel} DSD,',
            f'#{String(district.name).camel} District,',
            f'#{String(province.name).camel} Province.',
            '',
            f'{lat0:.4f}° N, {lng0:.4f}° E',
        ]
    )


def get_random_polygon():
    gnd = get_random_gnd()
    log.debug(gnd)
    lat0, lng0 = gnd.centroid
    d = 0.004
    dlat, dlng = d, d
    lat1, lng1 = lat0 - dlat, lng0 - dlng
    lat2, lng2 = lat0 + dlat, lng0 + dlng

    p1 = (lng1, lat1)
    p2 = (lng2, lat1)
    p3 = (lng2, lat2)
    p4 = (lng1, lat2)

    def p(p):
        return f'{p[0]:.4f}+{p[1]:.4f}'

    polygon = f'POLYGON(({p(p1)},{p(p2)},{p(p3)},{p(p4)},{p(p1)}))'

    return polygon, get_location(gnd)
