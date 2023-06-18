from utils import SECONDS_IN, Time, TimeFormat


def get_date_id_non_weekend():
    ut = Time.now().ut
    day_of_week = TimeFormat('%a').stringify(Time(ut))
    if day_of_week == 'Sat':
        ut = ut - SECONDS_IN.DAY
    if day_of_week == 'Sun':
        ut = ut - 2 * SECONDS_IN.DAY
    return TimeFormat('%Y%m%d').stringify(Time(ut))


if __name__ == '__main__':
    print(get_date_id_non_weekend())
