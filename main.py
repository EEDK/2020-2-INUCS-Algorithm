import SortAlgorithm.Tool
import SortAlgorithm.Sort
import random, time
from matplotlib import pyplot as plt

def createRandomList(n):
    a = []
    for i in range(n):
        a.append(random.randint(1, n-1))

    return a

def merge(a, l, m, r):
    i = l
    j = m + 1
    k = l

    while i <= m and j <= r:
        if a[i] < a[j]:
            b[k] = a[i]
            k += 1
            i += 1
        else:
            b[k] = a[j]
            k += 1
            j += 1

    if i > m:
        for p in range(j, r + 1, 1):
            b[k] = a[p]
            k += 1
    else:
        for p in range(i, m + 1, 1):
            b[k] = a[p]
            k += 1

    for p in range(l, r + 1, 1):
        a[p] = b[p]

def mergeSort(a, l, r):
    if r > l:
        m = int((r+l) / 2)
        mergeSort(a, l, m)
        mergeSort(a, m + 1, r)
        merge(a, l, m, r)

def naturalMergeSort(a):
    run = SortAlgorithm.Tool.chopingRun(a, n)
    length = len(run)
    while length > 1:
        l = 0
        for i in range(1, length, 2):
            m = l + len(run[i-1]) - 1
            r = m + len(run[i])
            merge(a, l, m, r)
            l = r + 1
        run = SortAlgorithm.Tool.chopingRun(a, n)
        length = len(run)

def tournamentSort(a, n):
    newA = a.copy()
    result = []
    if n % 2 != 0:
        newA.append(0)
        n = n + 1

    for j in range(n):
        b = []
        for i in range(n):
            b.append(0)
        for i in range(n, 2*n):
            b.append(newA[i-n])

        for i in range(2*n-1, 0, -2):
            if b[i] > b[i-1]:
                v = b[i]
            else:
                v = b[i-1]

            b[i // 2] = v
        result.append(b[0])
        for i in range(n):
            if newA[i] == b[0]:
                newA[i] = 0
                break

    length = len(a)
    for i in range(length):
        a[i] = result[i]

if __name__ == '__main__':
    n = int(input('생성할 배열 개수 : '))
    startTime = time.time()
    a = SortAlgorithm.Tool.createRandomList(n)
    SortAlgorithm.Sort.heapSort(a, n)
    endHeapTime = time.time() - startTime

    startTime = time.time()
    a = createRandomList(n)
    tournamentSort(a, n)
    endTournamentTime = time.time() - startTime

    dataTime = [endHeapTime, endTournamentTime]
    plt.bar(range(len(dataTime)), dataTime)
    ax = plt.subplot()
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['heap', 'tournament'], rotation = 30)
    plt.show()