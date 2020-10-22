import time
from random import *

BLACK = 0
RED = 1

class node:
    def __init__(self, color, key=None, left=None, right=None):
        self.color = color
        self.key = key
        self.left = left
        self.right = right

class Dict:
    x = p = q = gg = node

    z = node(color=BLACK, key=0, left=0, right=0)
    z.left = z
    z.right = z
    head = node(color=BLACK, key=0, left=0, right=z)

    def search(self, searchKey):
        x = self.head.right

        while x != self.z:
            if x.key == searchKey:
                return x.key
            if x.key > searchKey:
                x = x.left
            else:
                x = x.right
        return -1

    def insert(self, v):
        x = p = g = self.head
        while x != self.z:
            gg = g
            g = p
            p = x
            if x.key == v:
                return

            if x.key > v:
                x = x.left
            else:
                x = x.right

            if x.left.color and x.right.color:
                self.split(x, p, g, gg, v)

        x = node(color=RED, key=v, left=self.z, right=self.z)
        if p.key > v:
            p.left = x
        else:
            p.right = x

        self.split(x, p, g, gg, v)
        self.head.right.color = BLACK

    def split(self, x, p, g, gg, v):
        x.color = RED
        x.left.color = BLACK
        x.right.color = BLACK

        if p.color:
            g.color = RED
            if (g.key > v) != (p.key > v):
                p = self.rotate(v, g)
            x = self.rotate(v, gg)
            x.color = BLACK

    def rotate(self, v, y):
        gc = c = node
        if y.key > v:
            c = y.left
        else:
            c = y.right

        if c.key > v:
            gc = c.left
            c.left = gc.right
            gc.right = c
        else:
            gc = c.right
            c.right = gc.left
            gc.left = c

        if y.key > v:
            y.left = gc
        else:
            y.right = gc
        return gc
    
    def check(self, n):
        for i in range(1, n+1):
            x = p = self.head

            while x != self.z:
                if x.key == i:
                    break
                if x.key > i:
                    p = x
                    x = x.left
                else:
                    p = x
                    x = x.right

            print('key = %d , parent = %d , color = %s'%(x.key, p.key, "black" if x.color == BLACK else "red"))


# N = int(input("만들 배열의 갯수 설정 : "))
#
# key = list(range(1, N + 1))
# shuffle(key)
#
# d = Dict()
# for i in range(N):
#     d.insert(key[i])
#
# print(key)
# start_time = time.time()
# s_key = randint(1, N + 1)
# result = d.search(s_key)
# if result == -1 or result != s_key:
#     print('탐색 오류')
# end_time = time.time() - start_time
#
# d.check(N)
# print('레드 블랙 트리 탐색 수행 시간(N = %d) : %0.3f'%(N, end_time))
