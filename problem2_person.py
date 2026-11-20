class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # Overload >  (runs when you write p1 > p2)
    def __gt__(self, other):
        return self.age > other.age

    def __str__(self):
        return f"{self.name} ({self.age}, {self.gender})"


if __name__ == "__main__":
    p1 = Person("Amina", 21, "Female")
    p2 = Person("Karim", 19, "Male")

    print("p1 =", p1)
    print("p2 =", p2)
    print("p1 > p2:", p1 > p2)
    print("p2 > p1:", p2 > p1)
