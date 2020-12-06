def bruteForce(p, t, k):
    M = len(p)
    N = len(t)

    i = k
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


text = 'ababababcababababcaabbababcaab'
pattern = 'abababca'

N = len(text)
M = len(pattern)

K = 0

while True:
    pos = bruteForce(pattern, text, K)
    K = pos + M
    if K < N:
        print('나타난 pos : ', pos)
    else:
        break
