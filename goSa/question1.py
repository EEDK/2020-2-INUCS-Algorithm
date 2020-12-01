import random

def cocktailSort(a, n):
    swapped = True
    start = 1
    end = n
    cnt = 1

    print(a)
    while (swapped == True):
        swapped = False
        for i in range(end - 1, start - 1, -1):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        print('i = %d, a ='%(cnt) , a)
        cnt += 1
        if (swapped == False):
            break
        swapped = False
        start = start + 1

        for i in range(start, end):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        print('i = %d, a =' %(cnt) , a)
        cnt += 1
        end = end - 1

N = 10
a = [0, 7, 5, 6, 4, 10, 9, 8, 1, 3, 2]
cocktailSort(a, 10)
print(a)
