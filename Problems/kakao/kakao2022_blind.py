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


n = 437674
k = 3

print(solution(n, k))
