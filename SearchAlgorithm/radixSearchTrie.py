class bitskey:
    def __init__(self, x):
        self.x = x

    def get(self):
        return self.x

    def bits(self, k, j):
        return (self.x >> k) & ~(~0 << j)

class node:
    def __init__(self, key):
        if key.get() == 0:
            self.key = bitskey(0)
            self.external = False

        else:
            self.key = key
            self.external = True

        self.left = 0
        self.right = 0

class Dict:
    itemMin = bitskey(0)
    head = 0
    headCheck = False

    def search(self, v):
        v = bitskey(v)
        return self.searchR(self.head, v, maxb-1)

    def searchR(self, h, v, d):
        if h == 0:
            return self.itemMin

        if v.get() == h.key.get():
            return v
        if v.bits(d, 1) == 0:
            return self.searchR(h.left, v, d-1)

        else:
            return self.searchR(h.right, v, d-1)

    def insert(self, v):
        v = bitskey(v)
        self.insertR(self.head, v, maxb-1)

    def insertR(self, h, v, d):
        if h == 0:
            h = node(v)
            if not self.headCheck:
                self.head = h
            return h

        if h.external:
            leaf = node(v)
            h = self.split(leaf, h, d)
            if not self.headCheck:
                self.head = h
                self.headCheck = True
            return h

        if v.bits(d, 1) == 0:
            h.left = self.insertR(h.left, v, d-1)
        else:
            h.right = self.insertR(h.right, v, d-1)
        return h

    def split(self, p, q, d):
        t = node(self.itemMin)
        if ((p.key.bits(d, 1)) * 2 + (q.key.bits(d, 1))) == 0:
            t.left = self.split(p, q, d-1)
        elif ((p.key.bits(d, 1)) * 2 + (q.key.bits(d, 1))) == 1:
            t.left = p
            t.right = q
        elif ((p.key.bits(d, 1)) * 2 + (q.key.bits(d, 1))) == 2:
            t.left = q
            t.right = p
        elif ((p.key.bits(d, 1)) * 2 + (q.key.bits(d, 1))) == 3:
            t.right = self.split(p, q, d - 1)

        return t



import random, time

N = 10000
maxb = 14

key = list(range(1, N+1))
sKey = list(range(1, N+1))
random.shuffle(key)

d = Dict()
for i in range(N):
    d.insert(key[i])

d.head.external = True
startTime = time.time()
for i in range(N):
    result = d.search(sKey[i])
    if result.get() == -1 or result.get() != sKey[i]:
        print('error')

endTime = time.time() - startTime

print('기수 탐색 트라이의 실행시간 (N = %d) : %0.3f' %(N, endTime))
print('Done')