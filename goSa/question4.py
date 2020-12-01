cipherKey = []
cipherKey.append(' ')

for i in range(1, 53):
    if i < 27:
        cipherKey.append(chr(ord('a') + i - 1))
    else:
        cipherKey.append(chr(ord('A') + i - 27))


def encipher(p, k):
    c = ''
    for i in range(len(p)):
        for j in range(53):
            if p[i] == cipherKey[j]:
                a = j
                break
        a += k
        a %= 53

        c += cipherKey[a]


    return c

while True:
    K = int(input('키 : '))
    if K == 999:
        print('프로그램 종료')
        break

    plainText = input('평문 : ')
    cipherText = encipher(plainText, K)
    print('암호문 : ', cipherText)
    print('')
