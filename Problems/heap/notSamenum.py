def solution(arr):
    answer = []
    lst = list()

    lst.append(arr[0])
    answer.append(arr[0])

    i = 1
    while i < len(arr):
        tmp = lst.pop(0)

        if tmp != arr[i]:
            answer.append(arr[i])

        lst.append(arr[i])
        i += 1

    return answer


print(solution([4, 4, 4, 3, 3]))
