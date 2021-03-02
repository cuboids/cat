from typing import Tuple, Any, Optional
from collections.abc import Callable


def is_even(n: int) -> Tuple[bool, str]:
    return not n % 2, "is_even "


def negate(b: bool) -> Tuple[bool, str]:
    return not b, "Not so! "


class Kleisli:

    M_APPEND = lambda self, x, y: x + y
    M_EMPTY = ""

    def __init__(self, f: Optional[Callable] = None) -> None:
        """ By default it initializes the Kleisli identity function. """
        if f is None:
            f = lambda x: (x, self.M_EMPTY)
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

    def __call__(self, *args, **kwargs):
        return self.f(*args, **kwargs)

    def __add__(self, other):
        def fg(*args, **kwargs):
            b = self.copy1()(other.copy1()(*args, **kwargs))
            st_g = other.copy2()(*args, **kwargs)
            st_f = self.copy2()(other.copy1()(*args, **kwargs))
            return b, self.M_APPEND(st_g, st_f)
        return Kleisli(fg)


example = 1
if example:
    negate = Kleisli(negate)
    is_even = Kleisli(is_even)
    kleisli_id = Kleisli()
    is_odd = kleisli_id + negate + kleisli_id + is_even
    print(is_odd(9))
