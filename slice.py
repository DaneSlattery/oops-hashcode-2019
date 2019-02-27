from operator import mul
from functools import reduce

class slice:
    n_tomato = 0
    n_mushroom = 0

    start_x = 0
    start_y = 0
    end_x = 0
    end_y = 0

    def length_x(self):
      return self.end_x - self.start_x + 1

    def length_y(self):
      return self.end_y - self.start_y + 1

    def lengths(self):
      return (self.length_x, self.length_y)

    def n_cells(self):
      return reduce(mul, self.lengths(), 1)