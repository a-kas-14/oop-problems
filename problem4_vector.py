class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Overload *  (runs when you write v1 * v2)
    # Returns the dot product: x1*x2 + y1*y2 + z1*z2
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)

    print("v1      =", v1)
    print("v2      =", v2)
    print("v1 * v2 =", v1 * v2)
