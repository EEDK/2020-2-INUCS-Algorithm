class point:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c


class line:
    def __init__(self):
        self.p1 = point(None, None, None)
        self.p2 = point(None, None, None)


x_value = [2, 12, 3, 10, 14, 1, 13, 6, 8, 7, 15, 16, 4, 11, 9, 5]
y_value = [6, 16, 12, 11, 4, 10, 8, 7, 9, 5, 3, 14, 15, 1, 13, 2]
c_value = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']

# x_value = [5, 7, 6, 8, 1, 4, 3, 2, 11, 12, 10, 9]
# y_value = [3, 11, 12, 2, 4, 10, 6, 5, 8, 9, 1, 7]
# c_value = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']