
def heapify(a, h, m):
    v = a[h]
    j = 2*h
    while j <= m:
        if j < m and a[j] < a[j+1]:
            j = j + 1
        if v >= a[j]:
            break
        else:
            a[int(j/2)] = a[j]
        j = 2*j

    a[int(j/2)] = v

def quickSort(a, l, r):
    if r > l:
        v, i, j = a[r], l-1, r

        while True:
            i += 1
            while a[i] < v:
                i += 1
            j -= 1
            while a[j] > v:
                j -= 1
            if i >= j:
                break

            a[i], a[j] = a[j], a[i]
        a[i], a[r] = a[r], a[i]
        quickSortInsert(a, l, i-1)
        quickSortInsert(a, i+1, r)

def insertionSort(a, l, r):
    for i in range(l+1, r+1):
        v, j = a[i], i
        while a[j-1] > v:
            a[j] = a[j-1]
            j -= 1
        a[j] = v

def quickSortInsert(a, l, r):
    if r - l <= 15:
        insertionSort(a, l, r)
    else:
        v, i, j = a[r], l - 1, r
        while True:
            i += 1
            while a[i] < v:
                i += 1
            j -= 1
            while a[j] > v:
                j -= 1
            if i >= j:
                break

            a[i], a[j] = a[j], a[i]
        a[i], a[r] = a[r], a[i]
        quickSortInsert(a, l, i-1)
        quickSortInsert(a, i+1, r)

def quickSortMiddle(a, l, r):
    if r - l > 1:
        mid = int((l+r)/2)
        if a[l] > a[mid]:
            a[l], a[mid] = a[mid], a[l]
        if a[mid] > a[r]:
            a[mid], a[r] = a[r], a[mid]
        if a[l] > a[mid]:
            a[l], a[mid] = a[mid], a[l]

        a[mid], a[r-1] = a[r-1], a[mid]
        v, i, j = a[r], l-1, r
        while True:
            i += 1
            while a[i] < v:
                i += 1
            j -= 1
            while a[j] > v:
                j -= 1
            if i >= j:
                break

            a[i], a[j] = a[j], a[i]
        a[i], a[r] = a[r], a[i]
        quickSortMiddle(a, l, i-1)
        quickSortMiddle(a, i+1, r)

def mergeSort(arr, left, right):
    if right > left:
        mid = int((right + left)/2)
        mergeSort(arr, left, mid)
        mergeSort(arr, mid+1, right)
        for i in range(mid+1, left, -1):
            b[i-1] = arr[i-1]
        i -= 1
        for j in range(mid, right):
            b[right+mid-j] = a[j+1]
        j += 1
        for k in range(left, right+1):
            if b[i] < b[j]:
                arr[k] = b[i]
                i += 1
            else:
                arr[k] = b[j]
                j -= 1

def heapSort(a, n):
    for i in range(int(n/2), 0, -1):
        heapify(a, i, n)
    for i in range(n-1, 0 , -1):
        a[1], a[i+1] = a[i+1], a[1]
        heapify(a, 1, i)

import random, time, sys
from matplotlib import pyplot as plt

sys.setrecursionlimit(3002)

N = int(input('배열의 갯수 N 값을 입력하시오 : '))

a = []
a.append(-1)

for i in range(N):
    a.append(random.randint(1, N))

startTimeQuick = time.time()
quickSort(a, 1, N)
endTimeQuick = time.time() - startTimeQuick

a = []
a.append(-1)

for i in range(N):
    a.append(random.randint(1, N))
b = a.copy()

startTimeMerge = time.time()
quickSortInsert(a, 1, N)
endTimeMerge = time.time() - startTimeMerge

a = []
a.append(-1)

for i in range(N):
     a.append(random.randint(1, N))

startTimeHeap = time.time()
quickSortMiddle(a, 1, N)
endTimeHeap = time.time() - startTimeHeap


print('기본 퀵 정렬 %.3f' %(endTimeQuick))
print('작은 부분화일 %.3f' %(endTimeMerge))
print('중간값분할 정렬 %.3f' %(endTimeHeap))

days_in_year = [endTimeQuick, endTimeMerge, endTimeHeap]
plt.bar(range(len(days_in_year)), days_in_year)
ax = plt.subplot()
ax.set_xticks([0, 1, 2])
ax.set_xticklabels(['default', 'insert', 'mid'], rotation=30)
plt.show()