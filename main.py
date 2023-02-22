# https://school.programmers.co.kr/learn/courses/30/lessons/154538
# greedy는 아님, 전체탐색?
# 아직 못품

def solution(x, y, n):
    answer = -1

    if x == y:
        return 0

    result = [x * 2, x * 3, x + n]
    a = [result]

    for tmp in result:
        tmpList = []

        if tmp * 2 <= y:
            tmpList.append(tmp*2)
        if tmp * 3 <= y:
            tmpList.append(tmp*3)
        if tmp + n <= y:
            tmpList.append(tmp+n)

        a.append(tmpList)

    for i in range(len(a)):
        for j in range(len(a[i])):

            if (a[i][j] == y):
                return i + 1

    return answer


x, y, n = 10, 40, 5
print(solution(x, y, n))
