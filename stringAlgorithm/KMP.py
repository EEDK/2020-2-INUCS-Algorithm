def initNext(p, m):
    next[0] = -1
    i = 0
    j = -1
    while i < m:
        if j != -1 and p[i] == p[j]:
            next[i] = next[j]
        else:
            next[i] = j
        while j >= 0 and p[i] != p[j]:
            j = next[j]
        j += 1
        i += 1

def KMP(pattern, text, k, m, n):
    initNext(pattern, m)
    i = k
    j = 0
    while j < m and i < n:
        while j >= 0 and text[i] != pattern[j]:
            j = next[j]
            print(i, j)
        i += 1
        j += 1

    if j == m:
        return i - m
    else:
        return i

next = [0] * 50
text = 'ababababcababababcaabbabababcaab'
pattern = 'abababca'

N = len(text)
M = len(pattern)

K = 0

while True:
    pos = KMP(pattern, text, K, M, N)
    K = pos + M
    if K < N:
        print('나타난 pos : ', pos)
    else:
        break
