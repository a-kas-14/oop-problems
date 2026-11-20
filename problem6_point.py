import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Distance from the origin (0, 0): sqrt(x² + y²)
    def distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __lt__(self, other):
        return self.distance() < other.distance()

    def __gt__(self, other):
        return self.distance() > other.distance()

    def __eq__(self, other):
        return self.distance() == other.distance()

    def __ne__(self, other):
        return self.distance() != other.distance()

    def __ge__(self, other):
        return self.distance() >= other.distance()

    def __le__(self, other):
        return self.distance() <= other.distance()

    def __str__(self):
        return f"({self.x}, {self.y})"


if __name__ == "__main__":
    p1 = Point(3, 4)
    p2 = Point(1, 1)
    p3 = Point(4, 3)

    print("p1 =", p1, "distance:", round(p1.distance(), 2))
    print("p2 =", p2, "distance:", round(p2.distance(), 2))
    print("p3 =", p3, "distance:", round(p3.distance(), 2))
    print()
    print("p1 <  p2:", p1 < p2)
    print("p1 >  p2:", p1 > p2)
    print("p1 == p3:", p1 == p3)
    print("p1 != p2:", p1 != p2)
    print("p1 >= p3:", p1 >= p3)
    print("p2 <= p1:", p2 <= p1)
