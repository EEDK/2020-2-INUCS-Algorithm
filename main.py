
def solution(decNum):
    answer = ''
    while decNum:
        if decNum % 3:
            answer += str(decNum % 3)
            decNum //= 3
        else:
            answer += "4"
            decNum = decNum//3 - 1
    return answer[::-1]


n = 7

print(solution(n))
