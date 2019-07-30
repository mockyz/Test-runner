# -*- coding: utf-8 -*-
import datetime


def get_date_timestamp(interval_days_to_now=0):
    """
    get the date timestamp according the interval day
    get_date_timestamp(0)) 这个表示当天
    get_date_timestamp(1)) 表示后天
    get_date_timestamp(－1)) 表示前天
    :param interval_days_to_now: interval days to now, could be positive or negative
    :return:
    """
    today = datetime.date.today()
    return_date = today + datetime.timedelta(days=interval_days_to_now)
    return float(return_date.strftime("%s"))
