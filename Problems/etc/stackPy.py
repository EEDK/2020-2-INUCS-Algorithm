def solution(s):
    answer = True

    lst = list()

    for i in range(len(s)):
        lst.append(s[i])

    while lst:
        pre = lst.pop()
        now = lst.pop()

        print(pre, now)

    return True


s = "((()))()"
print(solution(s))
