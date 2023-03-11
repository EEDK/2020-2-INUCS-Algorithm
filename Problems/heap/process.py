from math import ceil


def solution(progresses, speeds):
    answer = []
    days_left = [ceil((100-p)/s) for p, s in zip(progresses, speeds)]
    # 각 작업이 끝나기까지 남은 일수 계산

    while days_left:
        done = 1
        left = days_left.pop(0)
        # 첫 번째 작업은 먼저 배포

        while days_left and days_left[0] <= left:
            done += 1
            days_left.pop(0)
            # 같이 배포할 수 있는 기능들을 묶음

        answer.append(done)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
