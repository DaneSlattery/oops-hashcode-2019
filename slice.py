from operator import mul
from functools import reduce


class rectangle:
    def __init__(self, start_x, end_x, start_y, end_y):
        self.x1 = start_x
        self.x2 = end_x
        self.y1 = start_y
        self.y2 = end_y

    def toList(self):
        return (self.x1, self.x2, self.y1, self.y2)


class slice:
    n_tomato = None
    n_mushroom = None

    start_x = None
    start_y = None
    end_x = None
    end_y = None

    def length_x(self):
        return self.end_x - self.start_x + 1

    def length_y(self):
        return self.end_y - self.start_y + 1

    def lengths(self):
        return (self.length_x, self.length_y)

    def coords(self):
        return rectangle(self.start_x, self.end_x, self.start_y, self.end_y)

    def setCoords(self, x1, x2, y1, y2):
        self.start_x = x1
        self.end_x = x2
        self.start_y = y1
        self.end_y = y2

    def n_cells(self):
        return reduce(mul, self.lengths(), 1)

    def intersectsWith(self, other):
        if not isinstance(other, slice):
            raise Exception('slice1 and slice2 are meant to be slices')
        c1 = self.coords()
        c2 = other.coords()

        if c1.x1 <= c2.x2 and c2.x1 <= c1.x2 and c1.y1 <= c2.y2 and c2.y1 <= c1.y2:
            return True
        else:
            return False
