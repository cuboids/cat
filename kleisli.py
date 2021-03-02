from typing import Tuple


def is_even(n: int) -> Tuple[bool, str]:
    return not n % 2, "is even "


def negate(b: bool) -> Tuple[bool, str]:
    return not b, "Not so! "


class Kleisli:

    @staticmethod
    def copy1(f):
        def copy1_f(*args, **kwargs):
            result = f(*args, **kwargs)
            return result[0]
        return copy1_f

    @staticmethod
    def copy2(f):
        def copy2_f(*args, **kwargs):
            result = f(*args, **kwargs)
            return result[1]
        return copy2_f

    def compose(self, f, g):
        def both_fg(*args, **kwargs):
            b = self.copy1(f)(self.copy1(g)(*args, **kwargs))
            st_g = self.copy2(g)(*args, **kwargs)
            st_f = self.copy2(f)(self.copy1(g)(*args, **kwargs))
            return b, st_g + st_f
        return both_fg


K = Kleisli()
x = K.compose(negate, is_even)(4)
print(x)
