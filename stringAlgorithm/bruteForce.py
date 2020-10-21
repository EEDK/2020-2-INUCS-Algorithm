def bruteForce(p , t):
    M = len(p)
    N = len(t)

    i = 0
    j = 0
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1

    if j == M:
        return i - M
    else: return i


text = '123456789'
pattern = '4567'

print('나타난 pos : ', end = '')
print(bruteForce(pattern, text))