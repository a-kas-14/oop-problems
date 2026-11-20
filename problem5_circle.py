class Circle:
    def __init__(self, radius):
        self.radius = radius

    # <   less than
    def __lt__(self, other):
        return self.radius < other.radius

    # >   greater than
    def __gt__(self, other):
        return self.radius > other.radius

    # ==  equal
    def __eq__(self, other):
        return self.radius == other.radius

    # !=  not equal
    def __ne__(self, other):
        return self.radius != other.radius

    # >=  greater than or equal
    def __ge__(self, other):
        return self.radius >= other.radius

    # <=  less than or equal
    def __le__(self, other):
        return self.radius <= other.radius

    def __str__(self):
        return f"Circle(radius={self.radius})"


if __name__ == "__main__":
    c1 = Circle(5)
    c2 = Circle(3)
    c3 = Circle(5)

    print("c1 =", c1)
    print("c2 =", c2)
    print("c3 =", c3)
    print()
    print("c1 <  c2:", c1 < c2)
    print("c1 >  c2:", c1 > c2)
    print("c1 == c3:", c1 == c3)
    print("c1 != c2:", c1 != c2)
    print("c1 >= c3:", c1 >= c3)
    print("c2 <= c1:", c2 <= c1)
