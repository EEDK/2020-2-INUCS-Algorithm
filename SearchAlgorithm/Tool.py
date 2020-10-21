class bitskey:
    def __init__(self, x):
        self.x = x

    def get(self):
        return self.x

    def bits(self, k, j):
        return (self.x >> k) & ~(~0 << j)

    def allbits(self, n):
        a = ""
        x = self.x
        for i in range (n):
            if x == None:
                break
            a += str(x % 2)
            x = int(x / 2)
        print(a[::-1])



v = bitskey(11)
v.allbits(5)