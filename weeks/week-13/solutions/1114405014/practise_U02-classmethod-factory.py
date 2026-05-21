class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    @classmethod
    def from_string(cls, s):
        x, y = map(int, s.split(','))
        return cls(x, y)

    @classmethod
    def from_list(cls, lst):
        return cls(lst[0], lst[1])

    @classmethod
    def origin(cls):
        return cls(0, 0)

class ColoredPoint(Point):
    def __init__(self, x, y, color="black"):
        super().__init__(x, y)
        self.color = color

    def __repr__(self):
        return f"ColoredPoint({self.x}, {self.y}, color={self.color!r})"

class CostTable:
    CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, costs):
        self.costs = costs

    def cost_of(self, digit_index):
        return self.costs[digit_index]

    def total_cost(self, n, base):
        if n == 0:
            return self.costs[0]
        total = 0
        while n > 0:
            total += self.costs[n % base]
            n //= base
        return total

    @classmethod
    def uniform(cls, cost=1):
        return cls([cost] * 36)

    @classmethod
    def from_flat_string(cls, s):
        values = list(map(int, s.split()))
        return cls(values)
