def solution(logs):
    answer = []

    # UID별 이름을 담는 사전 -> 현실은 DB로 구현하는게 편할듯?
    nameDict = {}

    # 이름 설정
    for log in logs:
        tmpLog = log.split(sep=' ')

        act = tmpLog[0]
        uid = tmpLog[1]

        if act == "Enter" or act == "Change":
            nameDict[uid] = tmpLog[-1]

    # 로그 파싱 과정
    for log in logs:
        tmpLog = log.split(sep=' ')

        act = tmpLog[0]
        uid = tmpLog[1]

        tmpString = nameDict[uid]

        if act == "Enter":
            tmpString += "님이 들어왔습니다."
        elif act == "Leave":
            tmpString += "님이 나갔습니다."
        else:
            continue

        answer.append(tmpString)

    return answer


recode = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
          "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]

print(solution(recode))
