class node:
    def __init__(self, key=None):
        self.key = key

class Dict:
    def __init__(self):
        Dict.a = []

    def search(self, searchKey):
        i = 0
        n = len(Dict.a)
        while (i < n and Dict.a[i].key != searchKey):
            i += 1

        if i == n + 1:
            return -1
        else:
            return i

    def insert(self, v):
        Dict.a.append(node(v))

import random, time

N = 10000
key = list(range(1, N+1))
s_Key = list(range(1, N+1))

random.shuffle(key)
d = Dict()
for i in range(N):
    d.insert(key[i])

startTime = time.time()
for i in range(N):
    result = d.search(s_Key[i])
    if result == -1 or key[result] != s_Key[i]:
        print('탐색 오류')
endTime = time.time() - startTime
print('순차 탐색의 실행 시간 (N = %d) : %0.3f' %(N, endTime))