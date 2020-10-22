def initNext(p):
    M = len(p)
    next[0] = -1

    i = 0
    j = -1

    while i < M:
        if j != -1 and p[i] == p[j]:
            next[i] = next[j]
        else:
            next[i] = j
        while j >= 0 and p[i] != p[j]:
            j = next[j]

        i += 1
        j += 1

next = [0] * 100
pattern ='abracadabra'
initNext(pattern)
for i in range(1, len(pattern)):
    print(next[i], end= ' ')