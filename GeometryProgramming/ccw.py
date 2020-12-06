def ccw(p0, p1, p2):
    dx1 = p1.x - p0.x
    dy1 = p1.y - p0.y

    dx2 = p2.x - p0.x
    dy2 = p2.y - p0.y

    # p0 p1의 기울기가 , p0 p2의 기울기 보다 큰 경우 -> 시계반대방향으로 회전
    if dx1 * dy2 > dy1 * dx2:
        return +1
    # p0 p1의 기울기가 , p0 p2의 기울기 보다 작은 경우 -> 시계방향으로 회전
    if dx1 * dy2 < dy1 * dx2:
        return -1
    # p0 , p1이 동일한 점
    if dx1 == 0 and dy1 == 0:
        return 0
    # p2가 p0 , p1의 아래에 있는경우 시계 방향으로 간주
    if (dx1 * dx2 < 0) or (dy1 * dy2 < 0):
        return -1
    # p2가 p0, p1선분 위에 있는 경우 -> 시계 반대 방향으로 간주
    if (dx1 * dx1 + dy1 * dy1) < (dx2 * dx2 + dy2 * dy2):
        return +1

    return 0