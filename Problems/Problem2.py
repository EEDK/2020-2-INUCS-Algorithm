def mySolution(lottos, win_nums):
    answer = []

    numZero = 0
    for i in range(len(lottos)):
        if lottos[i] == 0:
            numZero += 1

    sameNumber = 0
    for i in range(len(win_nums)):
        for j in range(len(lottos)):
            if lottos[j] == win_nums[i]:
                sameNumber += 1
    if numZero == 6:
        answer = [1, 6]

    elif sameNumber == 0 and numZero == 0:
        answer = [6, 6]
    else:
        answer.append(7 - sameNumber - numZero)
        answer.append(7 - sameNumber)

    return answer


def bestSolution(lottos, win_nums):

    rank = [6, 6, 5, 4, 3, 2, 1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans], rank[ans]


if __name__ == '__main__':
    print(mySolution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))
