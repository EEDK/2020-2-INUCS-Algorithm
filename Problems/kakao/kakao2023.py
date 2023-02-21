# https://school.programmers.co.kr/learn/courses/30/lessons/150370?language=python3
# -> 모든달은 28일까지

def solution(today, terms, privacies):
    answer = []

    termsDict = {}

    for term in terms:
        termType, termMonth = term.split()
        termsDict[termType] = termMonth

    i = 1
    for privacy in privacies:
        priDate, termType = privacy.split()

        print(diffMonth(priDate, today))

        if diffMonth(today, priDate) >= int(termsDict[termType]):
            answer.append(i)

        i += 1

    return answer


def diffMonth(nowDate, beforeDate):
    nowYear, nowMonth, nowDate = map(int, nowDate.split('.'))
    beforeYear, beforeMonth, beforeDate = map(int, beforeDate.split('.'))

    nowALL = nowDate + nowMonth * 28 + nowYear * 12 * 28
    beforeALL = beforeDate + beforeMonth * 28 + beforeYear * 12 * 28

    return (nowALL - beforeALL) / 28


td = "2022.05.19"
te = ["A 6", "B 12", "C 3"]
pr = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

print(solution(td, te, pr))
