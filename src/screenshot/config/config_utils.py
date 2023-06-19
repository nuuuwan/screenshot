from utils import SECONDS_IN, Time, TimeFormat


def get_last_date_id_non_weekend():
    day_of_week = TimeFormat('%a').stringify(Time(ut))

    # If Sunday, get the previous Friday. Else the previous day.
    if day_of_week == 'Sun':
        ut = ut - 2 * SECONDS_IN.DAY
    else:
        ut = ut - SECONDS_IN.DAY

    return TimeFormat('%Y%m%d').stringify(Time(ut))


def get_last_month():
    ut = Time.now().ut
    ut = ut - SECONDS_IN.AVG_MONTH
    return TimeFormat('%B').stringify(Time(ut))


if __name__ == '__main__':
    print(get_date_id_non_weekend())
