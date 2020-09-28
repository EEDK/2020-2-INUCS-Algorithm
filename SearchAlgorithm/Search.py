def sequentialSearch(dict, searchKey, n):
    i = 0
    while (i < n and dict.a[i].key != searchKey):
        i += 1
        dict.count += 1

    if i == n+1:
        return -1
    else:
        return i

def binarySearch(dict, searchKey, n):
    left = 0
    right = n - 1

    while right >= left:
        dict.count += 1
        mid = (left+right) // 2

        if dict.a[mid].key == searchKey:
            return mid
        if dict.a[mid].key > searchKey:
            right = mid - 1
        else:
            left = mid + 1

    return -1