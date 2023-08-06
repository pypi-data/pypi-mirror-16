from datetime import datetime
from time import time
import udatetime

RFC3339_DATE = '2016-07-18'
RFC3339_TIME = '12:58:26.485897+02:00'
RFC3339_DATE_TIME = RFC3339_DATE + 'T' + RFC3339_TIME
RFC3339_DATE_TIME_DTLIB = RFC3339_DATE_TIME[:-6]
DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
DATETIME_OBJ = datetime.strptime(RFC3339_DATE_TIME_DTLIB, DATE_TIME_FORMAT)
TIME = time()


def benchmark_parse():
    def datetime_strptime():
        datetime.strptime(RFC3339_DATE_TIME_DTLIB, DATE_TIME_FORMAT)

    def udatetime_parse():
        udatetime.from_string(RFC3339_DATE_TIME)

    return (datetime_strptime, udatetime_parse)


def benchmark_format():
    def datetime_strftime():
        DATETIME_OBJ.strftime(DATE_TIME_FORMAT)

    def udatetime_format():
        udatetime.to_string(DATETIME_OBJ)

    return (datetime_strftime, udatetime_format)


def benchmark_utcnow():
    def datetime_utcnow():
        datetime.utcnow()

    def udatetime_utcnow():
        udatetime.utcnow()

    return (datetime_utcnow, udatetime_utcnow)


def benchmark_now():
    def datetime_now():
        datetime.now()

    def udatetime_now():
        udatetime.now()

    return (datetime_now, udatetime_now)


def benchmark_utcnow_to_string():
    def datetime_utcnow_to_string():
        datetime.utcnow().strftime(DATE_TIME_FORMAT)

    def udatetime_utcnow_to_string():
        udatetime.utcnow_to_string()

    return (datetime_utcnow_to_string, udatetime_utcnow_to_string)


def benchmark_now_to_string():
    def datetime_now_to_string():
        datetime.now().strftime(DATE_TIME_FORMAT)

    def udatetime_now_to_string():
        udatetime.now_to_string()

    return (datetime_now_to_string, udatetime_now_to_string)


def benchmark_fromtimestamp():
    def datetime_fromtimestamp():
        datetime.fromtimestamp(TIME)

    def udatetime_fromtimestamp():
        udatetime.fromtimestamp(TIME)

    return (datetime_fromtimestamp, udatetime_fromtimestamp)


def benchmark_utcfromtimestamp():
    def datetime_utcfromtimestamp():
        datetime.utcfromtimestamp(TIME)

    def udatetime_utcfromtimestamp():
        udatetime.utcfromtimestamp(TIME)

    return (datetime_utcfromtimestamp, udatetime_utcfromtimestamp)

if __name__ == '__main__':
    import timeit

    print 'Executing benchmarks ...'

    for k in globals().keys():
        if k.startswith('benchmark_'):
            print '============ %s' % k
            mins = []

            for func in globals()[k]():
                times =\
                    timeit.repeat('func()', setup='from __main__ import func')
                t = min(times)
                mins.append(t)

                print func.__name__, t, times

            mins = sorted(mins)
            print 'Difference: %d%%\n' % (100 - (mins[0] / (mins[1] / 100)))
