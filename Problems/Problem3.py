# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 본인의 위치는 (1,1) -> [0]에 위치, 목표 지점 (5,5)
# -> 그리드는 아님 (최적 거리라고 갔다가 막혔을때 문제점 생길수 있음)
# 미로찾기 코테 -> BFS 사용 (깊이우선 탐색)
# DFS: 스택 또는 재귀함수로 구현
# BFS: 큐를 이용해서 구현

from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, x, y):
    n = len(graph)
    m = len(graph[0])

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    if graph[-1][-1] == 1:
        return -1
    return graph[-1][-1]


mapData = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
    1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
print(bfs(mapData, 0, 0))
