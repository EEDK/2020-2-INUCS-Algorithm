
# 선택 정렬
def SelectSort(a, n):
    for i in range(n):
        minIndex = i
        for j in range(i+1, n+1, 1):
            if a[j] < a[minIndex]:
                a[j], a[minIndex] = a[minIndex], a[j]

# 버블 정렬
def bubbleSort(a, n):
    for i in range(n, 1, -1):
        for j in range(1, i, 1):
            if a[j] > a[j+1]:
                a[j+1], a[j] = a[j], a[j+1]

# 삽입 정렬
def insertSort(a, n):
    for i in range(2, n+1, 1):
        v = a[i]
        j = i
        while j > 1 and a[j-1] > v:
            a[j] = a[j-1]
            j -= 1
        a[j] = v


if __name__ == '__main__':
    a = [-1, 4, 3, 2, 1, 5]
    insertSort(a, 4)
    print(a)