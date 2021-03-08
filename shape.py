import abc
import math
import random

import pytest


class Shape(abc.ABC):
    def __init__(self):
        self.color = random.choice(["Yellow", "Red", "Blue", "Violet"])

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'area') and callable(subclass.area) and
                hasattr(subclass, 'circ') and callable(subclass.circ) or NotImplemented)

    @abc.abstractmethod
    def area(self):
        raise NotImplementedError

    @abc.abstractmethod
    def circ(self):
        raise NotImplementedError


class Circle:
    def __init__(self, radius: float = 1.0):
        super().__init__()  # Does nothing, because Circle does not inherit from Shape 
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def circ(self) -> float:
        return 2 * math.pi * self.radius


class Rect(Shape):
    def __init__(self, depth: float = 1.0, height: float = 1.0):
        super().__init__()  # Assigns a color, because Rect inherits from Shape
        self.depth = depth
        self.height = height

    def area(self) -> float:
        return self.depth * self.height

    def circ(self) -> float:
        return 2.0 * (self.depth + self.height)


class Square(Rect):
    def __init__(self, depth: float = 1.0):
        super().__init__()  # Calls Rect.__init__(), which calls Shape.__init__()
        self.height = self.depth = depth


class Weirdshape(Shape):
    def area(self) -> float:
        return 123.456


class TestShape:
    """Testing class for pytest"""
    random.seed(1)
    R = Rect(2, 4)
    C1 = Circle(3 / math.sqrt(math.pi))
    C2 = Circle(3 / math.pi)
    S = Square(3)

    def test_area(self):
        assert self.R.area() == 8
        assert self.S.area() == 9
        assert math.isclose(self.C1.area(), 9)

    def test_circ(self):
        assert math.isclose(self.C2.circ(), 6)
        assert self.R.circ() == 12

    def test_color(self):
        assert self.R.color == "Red"
        assert self.S.color == "Yellow"
        assert not hasattr(self.C1, "color")

    def test_subclasshook(self):
        with pytest.raises(TypeError):
            Weirdshape()
        assert issubclass(Circle, Shape)
