def dfs(start, tickets, visited, answer):
    # 모든 항공권을 사용했으면 경로 반환
    if len(answer) == len(tickets) + 1:
        return answer

    # 현재 공항에서 출발하는 항공권을 찾음
    for i in range(len(tickets)):
        if tickets[i][0] == start and not visited[i]:
            # 다음 공항으로 이동
            visited[i] = True
            answer.append(tickets[i][1])
            # 재귀적으로 다음 공항에서 출발하는 경로 찾기
            res = dfs(tickets[i][1], tickets, visited, answer)
            if res:  # 경로를 찾았으면 반환
                return res
            # 경로를 찾지 못한 경우 다시 돌아와서 다른 경로 찾기 위해 backtrack
            visited[i] = False
            answer.pop()

    # 모든 경로를 찾아봤는데도 못 찾은 경우 None 반환
    return None


def solution(tickets):
    # 알파벳 순서대로 경로를 반환해야 하므로 미리 정렬
    tickets.sort()
    # 모든 공항 방문을 체크하는 배열
    visited = [False] * len(tickets)
    # ICN에서 출발하므로 answer에 ICN 추가
    answer = ["ICN"]
    return dfs("ICN", tickets, visited, answer)


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
