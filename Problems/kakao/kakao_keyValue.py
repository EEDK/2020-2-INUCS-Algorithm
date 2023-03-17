def solution(s):
    answer = ''
    nameDict = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
                'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    tmp = ''
    for string in s:
        if ord(string) > 57:
            tmp += string
            if nameDict.get(tmp):
                answer += nameDict[tmp]
                tmp = ''
        else:
            answer += string

    return int(answer)
