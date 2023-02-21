def Solution(str):
    answer = '?'
    dict = {}

    for s in str:
        tmpS = s.lower()
        if (tmpS in dict):
            dict[tmpS] += 1
        else:
            dict[tmpS] = 1


    mostCount = [k for k, v in dict.items() if max(dict.values()) == v]

    if (len(mostCount) == 1):
        answer = mostCount[0]

    return answer.upper()


S = input('')
print(Solution(S))
