import SortAlgorithm.Tool
import random

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
            r = l + len(run[i-1]) + len(run[i])
            m = int((r+l) / 2)
            merge(a, l, m, r)
            l = r

        run = SortAlgorithm.Tool.chopingRun(a, n)
        length = len(run)


if __name__ == '__main__':
    n = int(input('생성할 배열 개수 : '))
    a = createRandomList(n)
    b = a.copy()
    mergeSort(a, 0, n - 1)

    a = createRandomList(n)
    b = a.copy()
    naturalMergeSort(a)
