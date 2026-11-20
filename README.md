# OOP Problems

Python exercises for my Object-Oriented Programming class.

---

## Part 1: Operator Overloading

Files are in the main folder.

| File | Class | Operators overloaded |
|---|---|---|
| `problem1_complex.py` | `Complex` | `+`, `-` |
| `problem2_person.py` | `Person` | `>` (compares ages) |
| `problem4_vector.py` | `Vector` | `*` (dot product) |
| `problem5_circle.py` | `Circle` | `<`, `>`, `==`, `!=`, `>=`, `<=` (compares radius) |
| `problem6_point.py` | `Point` | `<`, `>`, `==`, `!=`, `>=`, `<=` (compares distance from origin) |
| `problem7_matrix.py` | `Matrix` | `*` (matrix multiplication) |

### Problem descriptions

**Problem 1:** Implement a complex number class. Overload the addition and subtraction operators to add and subtract two complex numbers.

**Problem 2:** Create a class `Person` with `name`, `age` and `gender` as its attributes. Overload the `>` operator to compare two persons based on their age, such that `p1 > p2` returns `True` if the age of `p1` is greater than `p2` and `False` otherwise.

**Problem 4:** Create a class `Vector` that represents a vector in space, with `x`, `y`, and `z` as its attributes. Overload the `*` operator to return the dot product of two vectors, such that `vector1 * vector2` returns the dot product of the two input vectors.

**Problem 5:** Overload all comparison operators (`<`, `>`, `==`, `!=`, `>=`, `<=`) for a `Circle` class based on radius.

**Problem 6:** Implement a 2D point class. Overload the comparison operators to compare two points based on their Euclidean distance from the origin.
Euclidean distance = `sqrt(x² + y²)`

**Problem 7:** Overload the multiplication operator for two matrices.

### What is operator overloading?

When Python sees an operator, it calls a special method on the object.
For example, `a + b` runs `a.__add__(b)`.

| Operator | Method |
|---|---|
| `+` | `__add__` |
| `-` | `__sub__` |
| `*` | `__mul__` |
| `<` | `__lt__` |
| `>` | `__gt__` |
| `==` | `__eq__` |
| `!=` | `__ne__` |
| `>=` | `__ge__` |
| `<=` | `__le__` |

---

## Part 2: Inheritance

Files are in the `inheritance/` folder.

| File | Classes | What it shows |
|---|---|---|
| `problem1_vehicle.py` | `Vehicle`, `Car`, `Bicycle` | Overriding a method |
| `problem2_person.py` | `Person`, `Student`, `Employee` | Adding attributes with `super()` |
| `problem3_bank.py` | `BankAccount`, `SavingsAccount` | Reusing and extending a parent class |

### Problem descriptions

**Problem 1:** Create a class `Vehicle` that has a method `drive` that returns the string "Driving a vehicle". Create two subclasses, `Car` and `Bicycle`, that override this method to return "Driving a car" and "Riding a bicycle", respectively.

**Problem 2:** Create a class `Person` with attributes `name`, `age`, `address` and method `introduce`. Create a subclass `Student` that has an attribute `field_of_study` and a personalized `introduce` method. Create another subclass `Employee` that has an attribute `company` and a personalized `introduce` method.

**Problem 3:** Define two classes, `BankAccount` and `SavingsAccount`:
- `BankAccount` has attributes `account_number` and `balance`, and methods `deposit` and `withdraw`
- `SavingsAccount` inherits from `BankAccount` and adds an `interest_rate` attribute and an `add_interest` method
- Add a `check_balance` method to `SavingsAccount`
- Add a `transfer` method to `BankAccount` that transfers money to a destination account (returns `False` if the balance is insufficient, `True` otherwise)

### What is inheritance?

A class can **inherit** from another class: `class Car(Vehicle):`.
The child class gets all the parent's attributes and methods, and can:
- **override** a method by writing its own version with the same name
- **extend** the parent by adding new attributes and methods
- use **`super()`** to call the parent's version of a method instead of rewriting it
