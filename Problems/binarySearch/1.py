def solution(n, times):
    left = 1
    right = max(times) * n

    while left <= right:
        mid = (left + right) // 2

        tmp = 0

        for tester in times:
            tmp += mid // tester
            if tmp >= n:
                break

        if tmp >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
