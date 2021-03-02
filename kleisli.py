from collections.abc import Callable
from typing import Tuple, Union, Optional


def is_even(n: int) -> Tuple[bool, str]:
    return not n % 2, "is_even "


def negate(b: bool) -> Tuple[bool, str]:
    return not b, "Not so! "


def safe_root(x: float) -> Union[bool, Tuple[bool, float]]:
    if x >= 0:
        return True, x ** .5
    return False


def safe_reciprocal(x: float) -> Union[bool, Tuple[bool, float]]:
    if x:
        return True, 1/x
    return False


class Kleisli:

    M_APPEND = lambda self, x, y: x + y
    M_EMPTY = ""

    def __init__(self, f: Optional[Callable] = None) -> None:
        """ By default it initializes the Kleisli identity function. """
        self.id = False
        if f is None:
            f = lambda x: (x, self.M_EMPTY)
            self.id = True
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


example = True
if example:
    negate = Kleisli(negate)
    is_even = Kleisli(is_even)
    kleisli_id = Kleisli()
    is_odd = kleisli_id + negate + kleisli_id + is_even
    print(is_odd(9))


class Partial:

    M_EMPTY = 0

    def __init__(self, f: Optional[Callable] = None) -> None:
        """ By default it initializes the Kleisli identity function. """
        self.id = False
        if f is None:
            f = lambda x: (True, x)
            self.id = True
        self.f = f

    def __call__(self, *args, **kwargs):
        return self.f(*args, **kwargs)

    def __add__(self, other):
        def fg(*args, **kwargs):
            y = other.f(*args, **kwargs)
            if not y:
                return False
            z = self.f(y[1])
            if not z:
                return False
            return z
        return Partial(fg)


example = False
if example:
    safe_root = Partial(safe_root)
    safe_reciprocal = Partial(safe_reciprocal)
    safe_root2 = safe_root + Partial()
    print(safe_root2(-9))
