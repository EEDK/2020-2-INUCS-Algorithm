# 거스름돈 최소로
# https://velog.io/@kyunghwan1207/%EA%B7%B8%EB%A6%AC%EB%94%94-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98Greedy-Algorithm-%ED%83%90%EC%9A%95%EB%B2%95

def ProblemGreedyExample(money):
    answer = 0

    changeMoney = [500, 100, 50, 10]

    for coin in changeMoney:
        answer += money // coin
        money = money % coin

    return answer


print(ProblemGreedyExample(1260))
