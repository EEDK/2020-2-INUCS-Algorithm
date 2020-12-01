class node:
    def __init__(self, key=None):
        self.key = key

class Dict:
    def __init__(self):
        Dict.a = []

    def search(self, searchKey):
        left = 0
        right = len(Dict.a) - 1
        while right >= left:
            mid = int((left + right) / 2)
            if Dict.a[mid].key == searchKey:
                return mid
            if Dict.a[mid].key > searchKey:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    def insert(self, v):
        Dict.a.append(node(v))

import random, time

N = 10000
key = list(range(1, N+1))
s_Key = list(range(1, N+1))

random.shuffle(s_Key)
d = Dict()
for i in range(N):
    d.insert(key[i])

startTime = time.time()
for i in range(N):
    result = d.search(s_Key[i])
    if result == -1 or key[result] != s_Key[i]:
        print('탐색 오류')
endTime = time.time() - startTime
print('이진 탐색의 실행 시간 (N = %d) : %0.3f' %(N, endTime))