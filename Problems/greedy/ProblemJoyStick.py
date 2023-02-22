# https://school.programmers.co.kr/learn/courses/30/lessons/42860
# - 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
# - 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
# - 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
# 따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
# 방향의 관점 잘 봐야할듯?

# 채점 결과
# 정확성: 55.6
# 합계: 55.6 / 100.0

def solution(name):
    answer = 0

    # 지금 이름 확인
    nowName = ''
    for i in range(len(name)):
        nowName += 'A'

    if nowName == name:
        return 0

    # 왼쪽에 A가 더많나, 오른쪽에 A가 더많나 판단
    countLeft = 0
    countRight = 0

    for j in range(len(name)):
        if name[j] == 'A':
            if j < len(name) / 2:
                countLeft += 1
            elif j > len(name) / 2:
                countRight += 1

    pos = 0
    while nowName != name:
        # 조이스틱 로직 구현
        if (ord(name[pos]) - ord(nowName[pos]) > 12):
            answer += (26 - (ord(name[pos]) - ord(nowName[pos])))
        else:
            answer += (ord(name[pos]) - ord(nowName[pos]))
        nowName = nameSwap(nowName, pos, name[pos])

        if countLeft > countRight:
            pos -= 1
        else:
            pos += 1

        answer += 1

    return answer - 1

# String 변경 로직


def nameSwap(S, targetPos, Char):
    if targetPos < 0:
        targetPos = len(S) + targetPos
    new_S = S[:targetPos] + Char + S[targetPos+1:]
    return new_S
