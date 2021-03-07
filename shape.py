import abc
from abc import ABC
import math


class Shape(ABC):
    @abc.abstractmethod
    def area(self):
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, r: float = 1) -> None:
        super().__init__()
        self.r = r

    def area(self):
        return math.pi * self.r ** 2


class Rect(Shape):
    def __init__(self, d: float = 1, h: float = 1) -> None:
        super().__init__()
        self.d = d
        self.h = h

    def area(self):
        return self.d * self.h


r = Rect(2, 4)
c = Circle(3/math.sqrt(math.pi))
assert r.area() == 8
assert math.isclose(c.area(), 9)
assert issubclass(Rect, Shape)
