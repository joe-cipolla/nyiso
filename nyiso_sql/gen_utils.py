"""general worker functions"""

import datetime


def is_valid_date(date):
    """
    :param - str, YYYY-MM-DD
    """
    year, month, day = date.split('-')

    is_valid = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        is_valid = False

    return is_valid
