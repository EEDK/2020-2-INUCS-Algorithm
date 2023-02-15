# https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    answer = 0

    listAnswer = [0]
    for num in numbers:
        tmp = []
        for i in listAnswer:
            tmp.append(i + num)
            tmp.append(i - num)
        print(tmp)
        listAnswer = tmp

    print(listAnswer)
    for i in listAnswer:
        if (target == i):
            answer += 1

    return answer


number = [1, 1, 1, 1, 1]
target = 3

print(solution(number, target))
