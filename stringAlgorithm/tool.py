
def index(c):
    if ord(c) == 32:
        return 0
    else:
        return ord(c) - 64

def checkCount(text):
    length = len(text)
    Ncount = [0] * 54
    for i in range(length):
        Ncount[index(text[i])] += 1

    print(Ncount)

    return Ncount
