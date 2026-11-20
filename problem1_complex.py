class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Overload +  (runs when you write a + b)
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    # Overload -  (runs when you write a - b)
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    # How the number looks when printed
    def __str__(self):
        sign = "+" if self.imag >= 0 else "-"
        return f"{self.real} {sign} {abs(self.imag)}i"


if __name__ == "__main__":
    a = Complex(3, 2)
    b = Complex(1, 7)

    print("a     =", a)
    print("b     =", b)
    print("a + b =", a + b)
    print("a - b =", a - b)

