
def solution(a, b, c):

    sumAmount = a + b + c

    if (sumAmount - max(a, b, c) <= sumAmount / 2):
        return "Invalid"

    if (a == b and a == c):
        return "Equilateral"
    elif (a == b or a == c or b == c):
        return "Isosceles"
    else:
        return "Scalene"


while True:
    a, b, c = map(int, input().split())
    if (a == 0 and b == 0 and c == 0):
        break

    print(solution(a, b, c))
