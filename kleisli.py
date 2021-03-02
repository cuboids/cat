from typing import Tuple
from collections.abc import Callable


def is_even(n: int) -> Tuple[bool, str]:
    return not n % 2, "is_even "


def negate(b: bool) -> Tuple[bool, str]:
    return not b, "Not so! "


class Kleisli:

    def __init__(self, f: Callable):
        """ f is a function """
        self.f = f

    def copy1(self) -> Callable:
        def copy1_f(*args, **kwargs):
            result = self.f(*args, **kwargs)
            return result[0]
        return copy1_f

    def copy2(self) -> Callable:
        def copy2_f(*args, **kwargs):
            result = self.f(*args, **kwargs)
            return result[1]
        return copy2_f

    def __add__(self, other) -> Callable:
        def fg(*args, **kwargs):
            b = self.copy1()(other.copy1()(*args, **kwargs))
            st_g = other.copy2()(*args, **kwargs)
            st_f = self.copy2()(other.copy1()(*args, **kwargs))
            return b, st_g + st_f
        return fg


example = True
if example:
    negate = Kleisli(negate)
    is_even = Kleisli(is_even)
    is_odd = negate + is_even
    print(is_odd(7))
