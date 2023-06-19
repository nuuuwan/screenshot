from utils import SECONDS_IN, Time, TimeFormat


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
