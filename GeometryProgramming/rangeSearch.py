import GeometryProgramming.geo as g

class Range:

    class node:
        key = 0
        left = None
        right = None

        def __init__(self, kk, ll, rr):
            self.key = kk
            self.left = ll
            self.right = rr

    z = node(0, None, None)
    z.left = z
    z.right = z
    head = node(0, None, z)

    def insert(self, v):
        p = self.head
        x = self.head.right

        while x != self.z:
            p = x

            if x.key == v:
                return

            if x.key > v:
                x = x.left

            else:
                x = x.right

        x = self.node(0, None, None)
        x.key = v
        x.left = self.z
        x.right = self.z

        if p.key > v:
            p.left = x

        else:
            p.right = x

    def search(self, v1, v2):
        return self.searchr(self.head.right, v1, v2)

    def searchr(self, t, v1, v2):
        count = 0

        if t == self.z:
            return 0

        if t.key >= v1:
            count += self.searchr(t.left, v1, v2)

        if t.key >= v1 and t.key <= v2:
            count += 1

        if t.key <= v2:
            count += self.searchr(t.right, v1, v2)

        return count

N = 8

r = Range()
key_list = [2, 1, 7, 8, 6, 3, 5, 4]

for i in range(N):
    r.insert(key_list[i])

result = r.search(3, 7)
print('방문 노드의 개수 : ', result)