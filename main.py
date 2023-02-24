def solution(person):

    waitTime = 0
    result = []

    person.sort()

    i = 0
    for per in person:
        waitTime += per
        result.append(waitTime)

    return sum(result)


"""
홀짝으로 구분 가능하나, 정확한 정답은 아님
"""


def stoneGame(number):

    if number % 2 == 0:
        return 'CY'

    else:
        return 'SK'


"""
의도한 Dynamic Programming
"""


def dynamicGame(number):
    dp = [0] * (n + 1)

    dp[0], dp[1], dp[2] = 0, 1, 2

    for i in range(3, n+1):
        print(i)
        dp[i] = min(dp[i - 1] + 1, dp[i - 3] + 1)

    print(dp)

    if dp[n] % 2 == 1:
        return "SK"
    else:
        return "CY"


n = int(input(''))
print(dynamicGame(n))
