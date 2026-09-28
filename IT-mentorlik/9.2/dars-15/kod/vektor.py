import math


class Vektor:
    """2D vektor — dunder metodlar namunasi."""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, t: tuple) -> "Vektor":
        return cls(t[0], t[1])

    @staticmethod
    def nol() -> "Vektor":
        return Vektor(0, 0)

    def uzunlik(self) -> float:
        return math.hypot(self.x, self.y)

    def __add__(self, other: "Vektor") -> "Vektor":
        return Vektor(self.x + other.x, self.y + other.y)

    def __mul__(self, k: float) -> "Vektor":
        return Vektor(self.x * k, self.y * k)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Vektor) and (self.x, self.y) == (other.x, other.y)

    def __lt__(self, other: "Vektor") -> bool:
        return self.uzunlik() < other.uzunlik()

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Vektor({self.x}, {self.y})"


a = Vektor(3, 4)
b = Vektor.from_tuple((1, 2))
print(a + b, a * 2, a.uzunlik(), a == Vektor(3, 4))
print(sorted([a, b, Vektor.nol()]))
