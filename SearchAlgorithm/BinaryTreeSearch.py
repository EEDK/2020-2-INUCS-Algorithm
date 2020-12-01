import time
from random import *

class node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

class Dict:
    x = p = node
    z = node(key=0, left=0, right=0)
    z.left = z
    z.right = z
    head = node(key=0, left=0, right=z)

    def insert(self, v):
        x = p = self.head
        while (x != self.z):
            p = x
            if x.key == v:
                return
            if x.key > v:
                x = x.left
            else:
                x = x.right
        x = node(key=v, left =self.z, right=self.z)
        if p.key > v:
            p.left = x
        else:
            p.right = x

    # if return value was 1 , dosen't search value
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


N = int(input("만들 배열의 갯수 설정 : "))

key = list(range(1, N + 1))
s_key = list(range(1, N + 1))
shuffle(key)

d = Dict()
for i in range(N):
    d.insert(key[i])

start_time = time.time()
for i in range(N):
    result = d.search(s_key[i])
    if result == -1 or result != s_key[i]:
        print('탐색 오류')
end_time = time.time() - start_time

print('이진 트리 수행 시간(N = %d) : %0.3f'%(N, end_time))