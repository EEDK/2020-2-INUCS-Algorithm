import SearchAlgorithm.Search
import random
import time

class node:
    def __init__(self, key=None):
        self.key = key

class Dict:
    def __init__(self):
        Dict.a = []
        Dict.count = 0

    def search(self, searchKey):
        return SearchAlgorithm.Search.binarySearch(self, searchKey, N)

    def insert(self, v):
        self.a.append(node(v))

def createRandomList(n):
    a = []
    for i in range(n):
        a.append(random.randint(1, n-1))

    return a

if __name__ == '__main__':
    N = int(input('입력받을 배열의 수 : '))
    key = list(range(1, N+1))
    s_key = createRandomList(N)

    d = Dict()
    for i in range(N):
        d.insert(key[i])

    startTime = time.time()
    for i in range(N):
        result = d.search(s_key[i])
        if result == -1 or key[result] != s_key[i]:
            print('탐색오류')

    endTime = time.time() - startTime
    print('이진 탐색의 실행 시간 (N=%d) : %0.3f 비교횟수 %d 평균비교 %f' %(N, endTime, d.count, d.count/N))
    print('탐색 완료')

