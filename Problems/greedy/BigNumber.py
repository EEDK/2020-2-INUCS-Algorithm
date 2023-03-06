import itertools


"""
BIG-O (N^2) -> 효율성 통과 실패


def solution(number, k):
    lst = itertools.combinations(number, len(number) - k)

    result = []

    for num in list(lst):
        sum = ''
        for j in num:
            sum += j
        result.append(sum)

    return max(result)

"""


def solution(number, k):
    stack = [number[0]]
    for i in number[1:]:
        while len(stack) > 0 and stack[-1] < i and k > 0:
            k -= 1
            stack.pop()
        stack.append(i)

    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)


print(solution("1924", 2))
print(solution("1231234", 3))
