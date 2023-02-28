"""
두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 
예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다.
n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.

최소 공배수 = 소인수 분해후 진행

ex) 12, 21의 최소 공배수를 구하는법

12 = 2^2 * 3, 21 = 3 * 7
-> 2*2*3*7 = 42
"""


def gcd(a, b):  # 최대공약수를 구하는 함수
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):  # 최소공배수를 구하는 함수
    return a * b // gcd(a, b)


def solution(arr):
    answer = arr[0]
    for i in range(1, len(arr)):
        answer = lcm(answer, arr[i])
    return answer


arr = [2, 6, 8, 14]
print(solution(arr))

# arr = [1, 2, 3]
