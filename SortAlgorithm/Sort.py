import SortAlgorithm.Tool

def SelectSort(a, n):
    for i in range(1, n):
        minIndex = i
        for j in range(i+1, n+1, 1):
            if a[j] < a[minIndex]:
                a[j], a[minIndex] = a[minIndex], a[j]

def bubbleSort(a, n):
    for i in range(n, 1, -1):
        for j in range(1, i, 1):
            if a[j] > a[j+1]:
                a[j+1], a[j] = a[j], a[j+1]

def insertSort(a, n):
    for i in range(2, n+1, 1):
        v = a[i]
        j = i
        while j > 1 and a[j-1] > v:
            a[j] = a[j-1]
            j -= 1
        a[j] = v

def shellSort(a, n):
    h = 1
    while h < n:
        h = h * 3 + 1

    while h > 0:
        for i in range(h+1, n+1, 1):
            v = a[i]
            j = i
            while j > h and a[j-h] > v:
                a[j] = a[j-h]
                j = j-h
            a[j] = v
        h = int(h / 3)

def quickSort(a, l, r):
    if r > l:
        i = SortAlgorithm.Tool.partition(a, l, r)
        quickSort(a, l, i-1)
        quickSort(a, i+1, r)

def heapSort(a, n):
    i = int(n/2)
    while i >= 1:
        SortAlgorithm.Tool.heapify(a, i, n)
        i -= 1
    i = n - 1
    while i >= 1:
        a[1], a[i+1] = a[i+1], a[1]
        SortAlgorithm.Tool.heapify(a, 1, i)
        i -= 1

def countingSort(a, n, m):
    count = [0] * (m+1)
    b = [0] * (n+1)
    for i in range(1, n+1, 1):
        count[a[i]] = count[a[i]] + 1

    for j in range(2, m+1, 1):
        count[j] = count[j-1] + count[j]

    for i in range(n, 0, -1):
        b[count[a[i]]] = a[i]
        count[a[i]] = count[a[i]] - 1

    for i in range(1, n+1, 1):
        a[i] = b[i]

def radixSort(arr, n, m):
    Q = []
    for i in range(10):
        Q.append([])

    for k in range(1, m+1):
        for i in range(1, n+1):
            kd = SortAlgorithm.Tool.digit(arr[i], k)
            SortAlgorithm.Tool.enqueue(Q[kd], arr[i])
        p = 0
        for i in range(10):
            while len(Q[i]) != 0:
                p += 1
                arr[p] = SortAlgorithm.Tool.dequeue(Q[i])

def exchangeSort(a, n):
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if a[j] < a[i]:
                a[j], a[i] = a[i], a[j]

def cocktailSort(a, n):
    swapped = True
    start = 1
    end = n
    while (swapped == True):
        swapped = False
        for i in range(start, end):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        if (swapped == False):
            break
        swapped = False

        end = end - 1
        for i in range(end - 1, start - 1, -1):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        start = start + 1

def mergeSort(a, l, r):
    if r > l:
        m = int((r+l) / 2)
        mergeSort(a, l, m)
        mergeSort(a, m + 1, r)

        for i in range(m+1, l, -1):
            b[i-1] = a[i-1]
        i -= 1

        for j in range(m, r):
            b[r+m-j] = a[j+1]
        j += 1

        for k in range(l, r+1):
            if b[i] < b[j]:
                a[k] = b[i]
                i += 1
            else:
                a[k] = b[j]
                j -= 1

