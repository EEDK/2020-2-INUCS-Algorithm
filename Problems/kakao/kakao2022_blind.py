def solution(n, k):
    answer = -1

    stack = list()
    kDigit = ""

    while n:
        stack += str(n % k)
        n //= 3

    while stack:
        kDigit += stack.pop()

    print(kDigit)

    return answer


def isDigit(num):
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1

    return True


n = 437674
k = 3

print(solution(n, k))
