# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):

    list1 = [-1]

    for n in nums:
        for s in range(len(list1)):
            if n == list1[s]:
                break
            elif (s == len(list1) - 1):
                list1.append(n)

    answer = 0

    if (len(list1) - 1 < len(nums) / 2):
        answer = len(list1) - 1
    else:
        answer = len(nums) / 2
    return answer


a = [3, 1, 2, 3]
print(solution(a))
