# -*- coding:utf-8 -*-

"""
工具包

Author: HuangTao
Date:   2018/04/28
Update: 2018/09/07 1. 增加函数datetime_to_timestamp;
"""

import uuid
import time
import decimal
import datetime
from functools import wraps
from time import time as timestamp

def get_cur_timestamp():
    """ 获取当前时间戳
    """
    ts = int(time.time())
    return ts


def get_cur_timestamp_ms():
    """ 获取当前时间戳(毫秒)
    """
    ts = int(time.time() * 1000)
    return ts


def get_cur_datetime_m(fmt='%Y%m%d%H%M%S%f'):
    """ 获取当前日期时间字符串，包含 年 + 月 + 日 + 时 + 分 + 秒 + 微妙
    """
    today = datetime.datetime.today()
    str_m = today.strftime(fmt)
    return str_m


def get_datetime(fmt='%Y.%m.%d %H:%M:%S'):
    """ 获取日期时间字符串，包含 年 + 月 + 日 + 时 + 分 + 秒
    """
    today = datetime.datetime.today()
    str_dt = today.strftime(fmt)
    return str_dt


def get_date(fmt='%Y%m%d', delta_day=0):
    """ 获取日期字符串，包含 年 + 月 + 日
    @param fmt 返回的日期格式
    """
    day = datetime.datetime.today()
    if delta_day:
        day += datetime.timedelta(days=delta_day)
    str_d = day.strftime(fmt)
    return str_d


def date_str_to_dt(date_str=None, fmt='%Y%m%d', delta_day=0):
    """ 日期字符串转换到datetime对象
    @param date_str 日期字符串
    @param fmt 日期字符串格式
    @param delta_day 相对天数，<0减相对天数，>0加相对天数
    """
    if not date_str:
        dt = datetime.datetime.today()
    else:
        dt = datetime.datetime.strptime(date_str, fmt)
    if delta_day:
        dt += datetime.timedelta(days=delta_day)
    return dt


def dt_to_date_str(dt=None, fmt='%Y%m%d', delta_day=0):
    """ datetime对象转换到日期字符串
    @param dt datetime对象
    @param fmt 返回的日期字符串格式
    @param delta_day 相对天数，<0减相对天数，>0加相对天数
    """
    if not dt:
        dt = datetime.datetime.today()
    if delta_day:
        dt += datetime.timedelta(days=delta_day)
    str_d = dt.strftime(fmt)
    return str_d


def get_utc_time():
    """ 获取当前utc时间
    """
    utc_t = datetime.datetime.utcnow()
    return utc_t


def ts_to_datetime_str_ms(ts=None, fmt='%Y-%m-%d %H:%M:%S'):
    """ 将时间戳转换为日期时间格式，年-月-日 时:分:秒,毫秒
    @param ts 时间戳，默认None即为当前时间戳
    @param fmt 返回的日期字符串格式
    """
    if not ts:
        ts = get_cur_timestamp()

    dt = datetime.datetime.fromtimestamp(ts/1000)
    return dt.strftime(fmt)

def ts_to_datetime_str(ts=None, fmt='%Y-%m-%d %H:%M:%S,%f'):
    """ 将时间戳转换为日期时间格式，年-月-日 时:分:秒
    @param ts 时间戳，默认None即为当前时间戳
    @param fmt 返回的日期字符串格式
    """
    if not ts:
        ts = get_cur_timestamp()
    dt = datetime.datetime.fromtimestamp(ts/1000)
    return dt.strftime(fmt)


def datetime_str_to_ts(dt_str, fmt='%Y-%m-%d %H:%M:%S'):
    """ 将日期时间格式字符串转换成时间戳
    @param dt_str 日期时间字符串
    @param fmt 日期时间字符串格式
    """
    ts = int(time.mktime(datetime.datetime.strptime(dt_str, fmt).timetuple()))
    return ts


def datetime_to_timestamp(dt=None, tzinfo=None):
    """ 将datetime对象转换成时间戳
    @param dt datetime对象，如果为None，默认使用当前UTC时间
    @param tzinfo 时区对象，如果为None，默认使用timezone.utc
    @return ts 时间戳(秒)
    """
    if not dt:
        dt = get_utc_time()
    if not tzinfo:
        tzinfo = datetime.timezone.utc
    ts = int(dt.replace(tzinfo=tzinfo).timestamp())
    return ts


def utctime_str_to_ts(utctime_str, fmt="%Y-%m-%dT%H:%M:%S.%fZ"):
    """ 将UTC日期时间格式字符串转换成时间戳
    @param utctime_str 日期时间字符串 eg: 2019-03-04T09:14:27.806Z
    @param fmt 日期时间字符串格式
    @return timestamp 时间戳(秒)
    """
    dt = datetime.datetime.strptime(utctime_str, fmt)
    timestamp = int(dt.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None).timestamp())
    return timestamp


def utctime_str_to_mts(utctime_str, fmt="%Y-%m-%dT%H:%M:%S.%fZ"):
    """ 将UTC日期时间格式字符串转换成时间戳（毫秒）
    @param utctime_str 日期时间字符串 eg: 2019-03-04T09:14:27.806Z
    @param fmt 日期时间字符串格式
    @return timestamp 时间戳(毫秒)
    """
    dt = datetime.datetime.strptime(utctime_str, fmt)
    timestamp = int(dt.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None).timestamp() * 1000)
    return timestamp


def get_uuid1():
    """ make a UUID based on the host ID and current time
    """
    s = uuid.uuid1()
    return str(s)


def get_uuid3(str_in):
    """ make a UUID using an MD5 hash of a namespace UUID and a name
    @param str_in 输入字符串
    """
    s = uuid.uuid3(uuid.NAMESPACE_DNS, str_in)
    return str(s)


def get_uuid4():
    """ make a random UUID
    """
    s = uuid.uuid4()
    return str(s)


def get_uuid5(str_in):
    """ make a UUID using a SHA-1 hash of a namespace UUID and a name
    @param str_in 输入字符串
    """
    s = uuid.uuid5(uuid.NAMESPACE_DNS, str_in)
    return str(s)


def float_to_str(f, p=20):
    """ Convert the given float to a string, without resorting to scientific notation.
    @param f 浮点数参数
    @param p 精读
    """
    if type(f) == str:
        f = float(f)
    ctx = decimal.Context(p)
    d1 = ctx.create_decimal(repr(f))
    return format(d1, 'f')


def time_cost(func):
    ''' 打印运行时间

    :param func: 运行的函数名称
    :re1`turn:
    '''

    def f(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        t1 = time.time()
        spend = t1 - t0
        print("运行耗时%.3f ms：函数%s" % (spend*1000, func.__name__))

    return f