BLACK = 0
RED = 1

class node:
    def __init__(self, color, key=None, left=None, right=None, ):
        self.key = key
        self.left = left
        self.right = right
        self.color = color

class Dict:
    x = p = q = gg = node

    z = node(color=BLACK, key=0, left=0, right=0)
    z.left= z
    z.right = z
    head = node(color=BLACK, key=0, left=0, right=0)

    def insert(self, v):
        x = p = g = self.head
        while x != self.z:
            gg = g
            g = p
            p = x
            if x.key == v:
                return

            if x.key > v:
                x = x.left
            else:
                x = x.right

            if x.left.color and x.right.color :
                self.split(x, p, g, gg, v)

        x = node(color=RED, key=v, left=self.z, right=self.z)
        if p.key > v:
            p.left = x
        else:
            p.right = x

        self.split(x, p, g, gg, v)
        self.head.right.color = BLACK

    def search(self, searchKey):
        x = self.head.right

        while x != self.z:
            if x.key == searchKey:
                return x.key
            if x.key > searchKey:
                x = x.left
            else:
                x = x.right
        return -1

    def split(self, x, p, g, gg, v):
        x.color = RED
        x.left.color = BLACK
        x.right.color = BLACK

        if p.color:
            g.color = RED
            if (g.key > v) != (p.key > v):
                p = self.rotate(v , g)
            x = self.rotate(v, gg)
            x.color = BLACK

    def rotate(self, v , y):
        gc = c = node
        if y.key > v:
            c = y.left
        else:
            c = y.right

        if c.key > v:
            gc = c.left
            c.left = gc.right
            gc.right = c
        else:
            bc = c.right
            c.right = gc.left
            gc.left = c

        if y.key > v:
            y.left = gc
        else:
            y.right = gc
        return gc
