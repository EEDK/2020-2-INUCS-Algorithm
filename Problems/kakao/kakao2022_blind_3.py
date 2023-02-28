"""
기본시간 180분 기본요금 5000원, 단위시간 10분 단위요금 600원
"""

import math
import functools


def comparator(a, b):
    atime, acarId, aaction = a.split()
    btime, bcarId, baction = b.split()

    # t1이 크다면 1  // t2가 크다면 -1  //  같으면 0
    return (int(acarId) > int(bcarId)) - (int(acarId) < int(bcarId))


def solution(fees, records):
    records = sorted(records, key=functools.cmp_to_key(
        comparator))
    
    parkDB = {}
    

    for record in records:

        time, carID, act = record.split()

        print(time, carID, act)

    answer = []

    return answer


def calcFee(fees, timeGap):
    if timeGap <= fees[0]:
        return fees[1]

    else:
        return fees[1] + math.ceil((timeGap - fees[0]) / fees[2]) * fees[3]


def calcTimegap(start, end):
    startHour, startMinute = start.split(':')
    endHour, endMinute = end.split(':')
    return int(endHour) * 60 + int(endMinute) - (int(startHour) * 60 + int(startMinute))


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
           "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))
