# OOP Problems: Operator Overloading

Python exercises for my Object-Oriented Programming class.

## Problems

| File | Class | Operators overloaded |
|---|---|---|
| `problem1_complex.py` | `Complex` | `+`, `-` |
| `problem2_person.py` | `Person` | `>` (compares ages) |
| `problem4_vector.py` | `Vector` | `*` (dot product) |
| `problem5_circle.py` | `Circle` | `<`, `>`, `==`, `!=`, `>=`, `<=` (compares radius) |
| `problem6_point.py` | `Point` | `<`, `>`, `==`, `!=`, `>=`, `<=` (compares distance from origin) |
| `problem7_matrix.py` | `Matrix` | `*` (matrix multiplication) |

## Problem description 
Problem 1 : Implement a complex number class. Overload the addition and subtraction operators to add and subtract two complex numbers.

Problem 2 : Create a class Person with name, age and gender as its attributes. Overload the > operator to compare two persons based on their age, such that p1 > p2 returns True if the age of p1 is greater than p2 and False otherwise.

Problem 4 : Create a class Vector that represents a vector in space, with x, y, and z as its attributes. Overload the * operator to return the dot product of two vectors, such that vector1 * vector2 returns the dot product of the two input vectors.

Problem 5 : Overload all comparison operators (<, >, ==, !=, >=, <=) for a Circle class based on radius.

Problem 6 : Implement a 2D point class. Overload the comparison operators to compare two points based on their Euclidean distance from the origin.

Euclidean distance = sqrt(x² + y²)

Problem 7 : Overload the multiplication operator for two matrices.

## What is operator overloading?

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
