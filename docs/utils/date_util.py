# -*- coding: utf-8 -*-
import datetime


def get_format_date(interval_days=0, time_format="%Y-%m-%d %H:%M:%S"):
    """
    get format date like: default format is 2016-01-01 00:00:00
    :param interval_days:
    :param time_format:
    :return:
    """
    today = datetime.date.today()
    return_date = today + datetime.timedelta(days=interval_days)
    return return_date.strftime(time_format)


def get_format_datetime(days=0, minutes=0, seconds=0, time_format="%Y-%m-%d %H:%M:%S"):
    """
    get format date time like: default format is 2016-01-01 01:30:30
    :param days:
    :param minutes:
    :param seconds:
    :param time_format:
    :return:
    """
    return_date = get_interval_date(interval_days=days, interval_minutes=minutes, interval_seconds=seconds)
    return return_date.strftime(time_format)


def get_interval_date(interval_days=0, interval_minutes=0, interval_seconds=0):
    """
    get date by interval days from today
    :param interval_days:
    :param interval_minutes:
    :param interval_seconds:
    :return:
    """
    today = datetime.datetime.now()
    return today + datetime.timedelta(interval_days, interval_minutes, interval_seconds)


def get_datetime_in_long(interval_days=0, interval_minutes=0, interval_seconds=0):
    """
    get long number of date
    :param interval_days:
    :param interval_minutes:
    :param interval_seconds:
    :return:
    """
    return_date = get_interval_date(interval_days=interval_days, interval_minutes=interval_minutes,
                                    interval_seconds=interval_seconds)
    return return_date.strftime('%s')
