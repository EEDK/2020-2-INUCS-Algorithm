import SortAlgorithm.Tool
import random
import time


def merge(a, l, m, r):
    i = l
    j = m + 1
    k = l

    while i <= m and j <= r:
        if (a[i] < a[j]):
            b[k] = a[i]
            k = k + 1
            i = i + 1
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
    print(a)

if __name__ == '__main__':
    a = [6, 7, 8, 3, 4, 1, 5, 9, 10, 2]
    #a = SortAlgorithm.Tool.chopingRun(a, 10)
    b = a.copy()

    mergeSort(a, 0, 9)
    print(a)

