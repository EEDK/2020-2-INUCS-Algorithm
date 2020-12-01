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

def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if a[i-1] > a[i]:
            isSorted=False
        if not isSorted:
            break
    if isSorted:
        print("정렬완료")
    else:
        print("정렬 오류 발생")

def naturalMergeSort(a, n):
    run = chopingRun(a, n)
    length = len(run)
    while length > 1:
        l = 0
        for i in range(1, length, 2):
            m = l + len(run[i-1]) - 1
            r = m + len(run[i])
            merge(a, l, m, r)
            l = r + 1
        run = chopingRun(a, n)
        length = len(run)


import math

def tournament_Sort(arr, n):
    resultArray = []
    powerNum = 0

    while True:
        x = int(math.pow(2, powerNum))
        if x > n:
            break
        else:
            powerNum += 1

    b = [0] * (x * 2)
    for i in range(0, n):
        b[i + x] = arr[i + 1]
    for i in range(x - 1, 0, -1):

        if b[i * 2] > b[i * 2 + 1]:
            b[i] = b[i * 2]
        else:
            b[i] = b[i * 2 + 1]
    resultArray.append(b[1])

    while len(resultArray) < n:
        l = 1
        while l < x:
            if b[2 * l] == b[1]:
                l = 2 * l
            else:
                l = 2 * l + 1
        b[l] = 0
        while l > 1:
            l = l // 2
            if b[2 * l] < b[2 * l + 1]:
                b[l] = b[2 * l + 1]
            else:
                b[l] = b[2 * l]
        resultArray.append(b[1])

    return resultArray


import random, time
from matplotlib import pyplot as plt

N = int(input('배열의 갯수 N 값을 입력하시오 : '))

a = []
for i in range(N):
    a.append(random.randint(1, N))
b = a.copy()

startTimeMerge = time.time()
naturalMergeSort(a, N)
endTimeMerge = time.time() - startTimeMerge
checkSort(a, N)

a = []
a.append(None)
key = list(range(1, N+1))
random.shuffle(key)
for i in range(N):
    a.append(key[i])

startTimeTournament = time.time()
SortedArray = tournament_Sort(a, N)
print(SortedArray)
endTimeTournament = time.time() - startTimeTournament
print('자연합병정렬 %.3f' %(endTimeMerge))
print('토너먼트 %.3f' %(endTimeTournament))

days_in_year = [endTimeMerge, endTimeTournament]
plt.bar(range(len(days_in_year)), days_in_year)
ax = plt.subplot()
ax.set_xticks([0, 1])
ax.set_xticklabels(['naturalMerge', 'Tournament'], rotation=30)
plt.show()