import itertools


def solution(number):
    lst = itertools.combinations(number, 3)
    answer = 0

    for num in list(lst):
        if sum(num) == 0:
            answer += 1

    return answer


print(solution([-2, 3, 0, 2, -5]))
