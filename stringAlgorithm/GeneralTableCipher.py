def encipher(p, k):
    c = ''
    for i in range(len(p)):
        a = ord(p[i])

        if a == 32:
            a = 0
        else:
            a -= 64
        c += k[a]

    return c

def decipher(p, k):
    c = ''
    defaultKey = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '

    for i in range(len(p)):

        for j in range(len(k)):
            if p[i] == k[j]:
                break
        j -= 1

        c += defaultKey[j]


    return c

plainText = input('암호화 시킬 내용 : ')
K = (input('원하는 K값 : '))

# plainText = 'SAVE PRIVATE RYAN'
# K = 'QHCBEJKARWSTUVD IOPXZFGLMNY'

print('평문 : ', plainText)
cipherText = encipher(plainText, K)
print('암호문 : ', cipherText)
decipherText = decipher(cipherText, K)
print('복호문 : ', decipherText)