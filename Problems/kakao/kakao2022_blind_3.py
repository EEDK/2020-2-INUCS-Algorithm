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

    answer = []
    feeDB = {}

    preTime, preID, preAction = records[0].split()

    for i in range(len(records)):
        time, carId, action = records[i].split()

        if carId not in feeDB:
            feeDB[carId] = 0

        if len(records) == 1:
            answer.append(calcFee(fees, calcTimegap(start=time, end="23:59")))
            return answer
        if preID != carId:
            if preAction == 'IN':
                feeDB[preID] += calcTimegap(start=preTime, end="23:59")

        else:
            if action == 'OUT':
                feeDB[preID] += calcTimegap(start=preTime, end=time)

        if i == len(records) - 1 and preID == carId and preAction == 'OUT' and action == 'IN':
            feeDB[preID] += calcTimegap(start=time, end="23:59")

        preTime, preID, preAction = time, carId, action

    for key, value in feeDB.items():
        answer.append(calcFee(fees, value))

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


fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]
print(solution(fees, records))
