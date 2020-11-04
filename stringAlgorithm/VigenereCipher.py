def encipher(p, k):
    c = ''
    n = len(k)

    for i in range(len(p)):
        a = ord(p[i])
        if a == 32:
            a = 64

        b = ord(k[i % n]) - 64
        t = a + b

        if t > 90:
            t -= 27
        if t == 64:
            t = 32
        c += chr(t)

    return c

def decipher(p, k):
    c = ''
    n = len(k)

    for i in range(len(p)):
        a = ord(p[i])
        if a == 32:
            a = 64

        b = ord(k[i % n]) - 64
        t = a - b

        if t < 65:
            t += 27

        if t == 91:
            t = 32

        c += chr(t)

    return c


plainText = input('암호화 시킬 내용 : ')
K = (input('원하는 K값 : '))

print('평문 : ', plainText)
cipherText = encipher(plainText, K)
print('암호문 : ', cipherText)
decipherText = decipher(cipherText, K)
print('복호문 : ', decipherText)