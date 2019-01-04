#!usr/bin/evn python
# coding=utf-8
# 描述： python 时间操作
# 作者： randy
# 时间： 2018/12/17 7:18 PM

# % y->两位数的年份表示（00 - 99）
# % Y->四位数的年份表示（000 - 9999）
# % m->月份（01 - 12）
# % d->月内中的一天（0 - 31）
# % H->24小时制小时数（0 - 23）
# % I->12小时制小时数（01 - 12）
# % M->分钟数（00 - 59）
# % S->秒（00 - 59）
# % a->本地简化星期名称
# % A->本地完整星期名称
# % b->本地简化的月份名称
# % B->本地完整的月份名称
# % c->本地相应的日期表示和时间表示
# % j->年内的一天（001 - 366）
# % p->本地A.M.或P.M.的等价符
# % U->一年中的星期数（00 - 53）星期天为星期的开始
# % w->星期（0 - 6），星期天为星期的开始
# % W->一年中的星期数（00 - 53）星期一为星期的开始
# % x->本地相应的日期表示
# % X->本地相应的时间表示
# % Z->当前时区的名称
# % %->%号本身
import time  # 引入时间


def get_timestr(timeformat='%Y-%m-%d %H:%M:%S', localtimetuple=None):
    print('获取时间字符串')
    if localtimetuple is None:
        timestr = time.strftime(timeformat, time.localtime())
    else:
        timestr = time.strftime(timeformat, localtimetuple)
    return timestr


def get_timestamp():
    """
    获取时间戳
    :return: 时间戳
    """
    timestamp = time.time()
    print("当前时间戳为：", timestamp)
    return timestamp


def get_timetuple():
    """
    获取时间元组
    :return: 时间元组
    """
    timetuple = time.gmtime()
    print("时间元组为：", timetuple)
    return timetuple


def get_localtimetuple():
    """
    获取本地时间元组（已经校正了时区信息）
    :return:
    """
    # 获取本地时间
    localtimetuple = time.localtime()
    print("本地时间元组为：", localtimetuple)
    return localtimetuple


def timestamp2timetuple(timestamp=None):
    """
    时间戳转换成时间元组
    :param timestamp: 时间戳
    :return: 时间元组
    """
    if timestamp is None:
        time_tuple = time.localtime()
    else:
        time_tuple = time.localtime(timestamp)
    return time_tuple


def timetuple2timestamp(time_tuple):
    """
    时间元组转换成时间戳
    :param time_tuple: 时间元组
    :return: 时间戳
    """
    timestamp = time.mktime(time_tuple)
    return timestamp


def timestamp2timestr(timestamp=None, str_format='%Y-%m-%d %H:%M:%S'):
    """
    时间戳转换成格式化时间字符串
    :param timestamp: 时间戳
    :param str_format: 时间字符串格式
    :return: 格式化时间字符串
    """
    if timestamp is None:
        time_tuple = time.localtime()
    else:
        time_tuple = time.localtime(timestamp)
    timestr = time.strftime(str_format, time_tuple)
    return timestr


def timestr2timestamp(timestr):
    """
    将格式化时间转化为时间戳
    :param timestr: 时间字符串，如"Mon May  8 14:27:08  2017"
    :return: 时间戳
    """
    timetuple = time.strptime(timestr, '%Y-%m-%d %H:%M:%S')
    timestamp = time.mktime(timetuple)
    print(timestamp)
    return timestamp


def timestr2timetuple(time_str, tuple_format):
    """
    时间字符串转换成时间元组
    :param time_str: 时间字符串
    :param tuple_format: 时间元组格式
    :return: 返回时间元组
    """
    time_tuple = time.strptime(time_str, tuple_format)
    return time_tuple


def timetuple2timestr(time_tuple, str_format='%Y-%m-%d %H:%M:%S'):
    """
    时间元组转换成时间字符串
    :param time_tuple: 时间元组
    :param str_format: 时间字符串格式
    :return: 格式化的时间字符串
    """
    timestr = time.strftime(str_format, time_tuple)
    print(timestr)
    return timestr


def time_com(first_time, secend_time):
    print(first_time)
    print(time.strftime("%H%M%S", first_time))
    print(secend_time)
    print(time.strftime("%H%M%S", secend_time))
    return int(time.strftime("%H%M%S", first_time)) - int(time.strftime("%H%M%S", secend_time))


def is_time_between(start, end, time_tuple=None):
    """
    判断时间是否在start和end之间
    :param start: integer，注意时间格式，如120000
    :param end: integer，注意时间格式，如170000
    :param time_tuple: 元组
    :return: True if time is between start and end
    """
    if time_tuple is None:
        return start < int(time.strftime("%H%M%S")) < end
    else:
        return start < int(time.strftime("%H%M%S", time_tuple)) < end


if __name__ == '__main__':
    get_timestamp()
    get_timetuple()
    get_localtimetuple()

    result = time_com(get_timetuple(), timestr2timetuple("14:23:40", "%H:%M:%S"))
    print(result)

    print('时间是否是在12:00:00到17:00:00之间->' + str(is_time_between(120000, 170000)))
    print('时间戳转换成时间元组->' + str(timestamp2timetuple()))
