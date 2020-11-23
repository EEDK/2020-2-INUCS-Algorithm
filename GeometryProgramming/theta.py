def theta(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    ax = abs(dx)
    ay = abs(dy)

    if ax + ay == 0:
        t = 0
    else:
        t = dy / (ax + ay)

    if dx < 0 :
        t = 2 - t
    elif dy < 0:
        t = 4 +t

    return t * 90
