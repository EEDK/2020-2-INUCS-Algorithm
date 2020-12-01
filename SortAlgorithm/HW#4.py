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

def exchangeSort(a, n):
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if a[j] < a[i]:
                a[j], a[i] = a[i], a[j]

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


import random, time

N = int(input('배열의 갯수 N 값을 입력하시오 : '))

a = []
a.append(None)

for i in range(N):
    a.append(random.randint(1, N))

startTimeSelect = time.time()
cocktailSort(a, N)
endTimeSelect = time.time() - startTimeSelect
checkSort(a, N)

a = []
a.append(None)

for i in range(N):
    a.append(random.randint(1, N))

startTimeBubble = time.time()
exchangeSort(a, N)
endTimeBubble = time.time() - startTimeBubble
checkSort(a, N)


print(endTimeBubble, endTimeSelect)