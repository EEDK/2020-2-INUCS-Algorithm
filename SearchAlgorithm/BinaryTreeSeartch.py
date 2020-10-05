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

    def insert(self, v):
        p = self.head
        x = self.head.right

        while x != self.z:
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
            p.right = x