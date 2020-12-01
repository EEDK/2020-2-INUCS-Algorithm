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
        return i
    else: return -1


html = open("question3.html", "r")
text = []
while True:
    line = html.readline()

    if not line:
        break

    else:
        text.append(line)

Length = len(text)
pattern = "mailto:"

for i in range(Length):
    pos = bruteForce(pattern, text[i])
    if (pos != -1):
        while True:
            if text[i][pos] != '"':
                print(text[i][pos], end='')
            else:
                break
            pos += 1

        print()
