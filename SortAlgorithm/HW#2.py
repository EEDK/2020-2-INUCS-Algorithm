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

import random, time

N = int(input('배열의 갯수 N 값을 입력하시오 : '))

a = []
a.append(None)

for i in range(N):
    a.append(random.randint(1, N))

startTimeSelect = time.time()
SelectSort(a, N)
endTimeSelect = time.time() - startTimeSelect

a = []
a.append(None)

for i in range(N):
    a.append(random.randint(1, N))

startTimeBubble = time.time()
bubbleSort(a, N)
endTimeBubble = time.time() - startTimeBubble


a = []
a.append(None)

for i in range(N):
    a.append(random.randint(1, N))

startTimeInsert = time.time()
insertSort(a, N)
endTimeInsert = time.time() - startTimeInsert


a = []
a.append(None)

for i in range(N):
    a.append(random.randint(1, N))

startTimeShell = time.time()
shellSort(a, N)
endTimeShell = time.time() - startTimeShell

print(endTimeBubble, endTimeSelect, endTimeSelect , endTimeShell)