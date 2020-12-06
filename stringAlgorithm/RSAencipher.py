def encode(p):
    m = ''
    for i in range(len(p)):
        a = ord(p[i])
        if a == 32:
            a = 64
        a -= 64
        if a == 0:
            m += '00'
        elif a < 10:
            m += '0' + str(a)
        else:
            m += str(a)

    return m

def decode(p):
    m = ''

    for i in range(0, len(p), 2):
        a = int(p[i:i+2]) + 64
        if a == 64:
            a = 32
        m += chr(a)

    return m


def encipher(p, n, pk):
    c = ''
    i = 0

    while i < len(p):
        m = ''
        for j in range(4):
            m += p[i+j]
        i += 4
        a = int(m)
        t = a
        for k in range(pk):
            b = t % n
            t = a * b
        if b < 10:
            c += '000' + str(b)
        elif b < 100:
            c += '00' + str(b)
        elif b < 1000:
            c += '0' + str(b)
        else:
            c += str(b)

    return c

def decipher(p, n, sk):
    c = ''
    i = 0

    while i < len(p):
        m = ''
        for j in range(4):
            m += p[i+j]
        i += 4
        a = int(m)
        t = a
        for k in range(sk):
            b = t % n
            t = a * b
        if b < 10:
            c += '000' + str(b)
        elif b < 100:
            c += '00' + str(b)
        elif b < 1000:
            c += '0' + str(b)
        else:
            c += str(b)

    return c


plainText = 'SAVE PRIVATE RYAN '

N = 3713
# 공개키
S = 97
# 비밀키
P = 37
plainMessage = encode(plainText)

print('평문 : ', plainMessage)
cipherMessage = encipher(plainMessage, N, P)
print('암호문 : ', cipherMessage)
decipherMessage = decipher(cipherMessage, N, S)
print('복호문 : ', decipherMessage)

decodeMessage = decode(decipherMessage)
print('복호된 내용 : ', decodeMessage)
