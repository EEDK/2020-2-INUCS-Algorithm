from collections import deque


def solution(maps):

    answer = 0

    startPosX, startPosY = 0, 0
    leverPosX, leverPosY = 0, 0
    endPosX, endPosY = 0, 0

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'S':
                startPosX, startPosY = i, j
            elif maps[i][j] == 'L':
                leverPosX, leverPosY = i, j
            elif maps[i][j] == 'E':
                endPosX, endPosY = i, j

    BPS_this(maps, startPosX, startPosY, leverPosX, leverPosY)

    return answer


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BPS_this(graph, startX, startY, targetX, targetY):
    n = len(graph)
    m = len(graph[0])

    queue = deque()
    queue.append((startX, startY))

    answer = {}

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 'X':
                continue
            if graph[nx][ny] == 'O' or 'S' or 'E':
                queue.append((nx, ny))
                print(queue)


maps = ["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]

print(solution(maps))
