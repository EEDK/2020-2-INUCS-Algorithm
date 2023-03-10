# def solution(n, a, b):
#     a.sort(reverse=True)
#     b.sort()
#     answer = 0

#     for i in range(n):
#         answer += a[i] * b[i]

#     return answer


# n = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# print(solution(n, a, b))

def calc(a, b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(int(a / b))
    print(a % b)


a, b = input().split()
calc(int(a), int(b))
