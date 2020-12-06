import GeometryProgramming.geo as g

class rect:
    def __init__(self):
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None


def insideRect(p, t_range):
    t1 = p.x >= t_range.x1 and p.x <= t_range.x2
    t2 = p.y >= t_range.y1 and p.y <= t_range.y2

    return t1 and t2


class Range:
    dummy = g.point(0, 0, None)

    class node:
        p = g.point
        left = None
        right = None

        def __init__(self, pp, ll, rr):
            self.p = pp
            self.left = ll
            self.right = rr

    z = node(dummy, 0, 0)
    z.left = z
    z.right = z

    head = node(dummy, 0, z)

    def insert(self, p):
        d = True
        f = self.node
        t = self.head
        while t != self.z:
            if d:
                td = p.x < t.p.x
            else:
                td = p.y < t.p.y
            f = t
            if td:
                t = t.left
            else:
                t = t.right
            d = not d
        t = self.node(self.dummy, 0, 0)
        t.p = p
        t.left = self.z
        t.right = self.z
        if td:
            f.left = t
        else:
            f.right = t

    def search(self, t_range):
        return self.searchr(self.head.right, t_range, 0)

    def searchr(self, t, t_range, d):
        count = 0
        if t == self.z:
            return 0

        tx1 = t_range.x1 < t.p.x
        tx2 = t_range.x2 >= t.p.x
        ty1 = t_range.y1 < t.p.y
        ty2 = t_range.y2 >= t.p.y

        if d:
            t1 = tx1
            t2 = tx2
        else:
            t1 = ty1
            t2 = ty2

        if t1:
            count += self.searchr(t.left, t_range, not d)
        if insideRect(t.p, t_range):
            count += 1
        if t2:
            count += self.searchr(t.right, t_range, not d)
        return count


N = 16
r = Range()
t_range = rect()
p = []
for i in range(N):
    p.append(g.point(g.x_value[i], g.y_value[i], g.c_value[i]))

for i in range(N):
    r.insert(p[i])

t_range.x1 = 7
t_range.x2 = 11
t_range.y1 = 10
t_range.y2 = 16

result = r.search(t_range)
print('점 개수 : ', result)
