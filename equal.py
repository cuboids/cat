from typing import Optional, Any


class Either:

    # Overwrite this to restrict to specific types.
    LEFT_TYPE = Any
    RIGHT_TYPE = Any

    def __init__(self, direction: str, value: Any):
        self.direction = direction
        self.value = value

    def left(self) -> Optional[LEFT_TYPE]:
        if self.direction.casefold() == "left":
            return self.value

    def right(self) -> Optional[RIGHT_TYPE]:
        if self.direction.casefold() == "right":
            return self.value


x = Either("Left", "shakespeare")
print(x.left())
print(x.right())
