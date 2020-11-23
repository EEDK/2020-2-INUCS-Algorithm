def ccw(p0, p1, p2):
    dx1 = p1.x - p0.x
    dy1 = p1.y - p0.y

    dx2 = p2.x - p0.x
    dy2 = p2.y - p0.y

    if dx1 * dy2 > dy1 * dx2:
        return +1
    if dx1 * dy2 < dy1 * dx2:
        return -1
    if dx1 == 0 and dy1 == 0:
        return 0
    if (dx1 * dx2 < 0) or (dy1 * dy2 < 0):
        return -1
    if (dx1 * dx1 + dy1 * dy1) < (dx2 * dx2 + dy2 * dy2):
        return +1
    return 0