from typing import Tuple, Any


# The way we implement the product of int and str here is by
# making them into tuples, where the second element is a bool
# indicating if an element is an integer. The reason for this
# implementation choice is that is is easily generalizable to
# products of other sets than int and str.
Product = [(12, True), (239023, True), ('Shakespeare', False)]

def equal(t: Tuple) -> Any:
    """Similar to Haskell's Equal?!"""
    # Or whatever you'd like them to be.
    left, right = lambda a:a, lambda b:b
    if t[1]:
        return left(t[0])
    return right(t[0])


print(equal(Product[2]))
