import random

def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if (a[i] > a[i+1]):
            isSorted=False
        if (not isSorted):
            break
    if isSorted:
        print("정렬완료")
    else:
        print("정렬 오류 발생")

def partition(a, l, r):
    v = a[r]
    i = l - 1
    j = r
    while True:
        while True:
            i = i + 1
            if a[i] >= v:
                break
        while True:
            j = j - 1
            if a[j] <= v:
                break
        if i >= j:
            break
        a[i], a[j] = a[j], a[i]
    a[i], a[r] = a[r], a[i]
    return i

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

def digit(num, k):
    for _ in range(k-1):
        num //= 10
    return num % 10

def enqueue(queue, data):
    queue.append(data)

def dequeue(queue):
    if len(queue) == 0:
        print('큐가 공백임')
        return -1
    else:
        data = queue.pop(0)
        return data

def createRandomList(n):
    a = []
    a.append(None)
    for i in range(n):
        a.append(random.randint(1, n-1))

    return a

def createReverseList(n):
    a = []
    for i in range(n+1):
        a.append(random.randint(1, n))
    a.sort(reverse=True)
    a[0] = -1

    return a

def chopingRun(a, n):
    newArray = []
    run = []

    for i in range(n-1):
        run.append(a[i])

        if a[i] > a[i+1]:
            newArray.append(run)
            run = []

    run.append(a[n-1])
    newArray.append(run)

    return newArray

