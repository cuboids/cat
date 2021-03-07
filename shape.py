import abc
from abc import ABC
import math
import random


class Shape(ABC):
    def __init__(self):
        self.number = random.choice(range(10))

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'area') and callable(subclass.area) and
                hasattr(subclass, 'area') and callable(subclass.area) or NotImplemented)

    @abc.abstractmethod
    def area(self):
        raise NotImplementedError

    @abc.abstractmethod
    def circ(self):
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius: float = 1):
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circ(self):
        return 2 * math.pi * self.radius


class Rect(Shape):
    def __init__(self, depth: float = 1, height: float = 1):
        super().__init__()
        self.depth = depth
        self.height = height

    def area(self):
        return self.depth * self.height

    def circ(self):
        return 2.0 * (self.depth + self.height)


class Square(Rect):
    def __init__(self, depth: float = 1):
        super().__init__()
        self.height = self.depth = depth


class Weirdshape(Shape):
    pass


r = Rect(2, 4)
c1 = Circle(3/math.sqrt(math.pi))
c2 = Circle(3/math.pi)
s = Square(3)
assert r.area() == 8
assert math.isclose(c1.area(), 9)
assert math.isclose(c2.circ(), 6)
assert s.area() == 9
try:
    Weirdshape()
    assert False
except TypeError:
    assert True
