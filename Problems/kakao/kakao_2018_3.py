import string


def solution(n, t, m, p):
    result = ''
    answer = ''
    i = 0

    while i <= t * m:
        result += convert_recur(i, n)
        i += 1

    startPos = p - 1

    while startPos < (p - 1) + (t * m):
        answer += result[startPos]
        startPos += m

    return answer


def convert_recur(num, base):
    number = string.digits + string.ascii_uppercase
    q, r = divmod(num, base)
    return convert_recur(q, base) + number[r] if q else number[r]


print(solution(2, 4, 2, 1))
