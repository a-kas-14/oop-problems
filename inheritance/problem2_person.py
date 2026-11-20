class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def introduce(self):
        return f"Hi, I'm {self.name}, I'm {self.age} years old and I live in {self.address}."


class Student(Person):
    def __init__(self, name, age, address, field_of_study):
        # Let Person set name, age and address
        super().__init__(name, age, address)
        # Add the attribute only Student has
        self.field_of_study = field_of_study

    # Personalized introduce
    def introduce(self):
        return super().introduce() + f" I study {self.field_of_study}."


class Employee(Person):
    def __init__(self, name, age, address, company):
        super().__init__(name, age, address)
        self.company = company

    def introduce(self):
        return super().introduce() + f" I work at {self.company}."


if __name__ == "__main__":
    p = Person("Sara", 40, "Montreal")
    s = Student("Amina", 21, "Toronto", "Computer Science")
    e = Employee("Karim", 30, "Paris", "Ubisoft")

    print(p.introduce())
    print(s.introduce())
    print(e.introduce())
