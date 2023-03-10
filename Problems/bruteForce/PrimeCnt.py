import math


def solution(numbers):
    answer = 0
    result = []

    for i in range(1, len(numbers) + 1):
        print(i)

    print(numbers)

    return answer


def isPrime(x):
    for i in range(2, int(math.sqrt(x) + 1)):  # 2부터 x의 제곱근까지의 숫자
        if x % i == 0:		# 나눠떨어지는 숫자가 있으면 소수가 아님
            return False

    return True


# print(solution("011"))
print(solution("17"))
