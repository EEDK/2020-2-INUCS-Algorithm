class node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

class Dict:
    x = p = node

    z = node(key=0, left=0, right=0)
    z.left = z
    z.right = z
    head = node(key=0, left=0, right=z)

    # if return value was 1 , dosen't search value
    def search(self, searchKey):
        x = self.head.right
        while x != self.z:
            if x.key == searchKey:
                return x.key
            if x.key > searchKey:
                print('left ', end='')
                x = x.left
            else:
                print('right ', end='')
                x = x.right
        return -1



    def insert(self, v):
        x = p = self.head
        while (x != self.z):
            p = x
            if x.key == v:
                return
            if x.key > v:
                x = x.left
            else:
                x = x.right

        x = node(key=v, left=self.z, right=self.z)
        if p.key > v:
            p.left = x
        else:
            p.right= x


key = [2, 1, 7, 8, 6, 3, 5, 4]
n = 8
d = Dict()
for i in range(n):
    d.insert(key[i])

while True:
    searchKey = int(input('탐색 키 입력 : '))

    if(searchKey == 999):
        print("프로그램 종료")
        break

    else:
        result = d.search(searchKey)
        print()
        if(result == -1):
            print('탐색 실패')
        else:
            print('탐색 성공')

    print()