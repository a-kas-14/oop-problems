class Matrix:
    def __init__(self, rows):
        # rows is a list of lists, for example [[1, 2], [3, 4]]
        self.rows = rows
        self.n_rows = len(rows)
        self.n_cols = len(rows[0])

    # Overload *  (runs when you write A * B)
    def __mul__(self, other):
        # A's number of columns must equal B's number of rows
        if self.n_cols != other.n_rows:
            raise ValueError("Cannot multiply: A's columns must equal B's rows")

        result = []
        for i in range(self.n_rows):              # each row of A
            new_row = []
            for j in range(other.n_cols):         # each column of B
                total = 0
                for k in range(self.n_cols):      # multiply and add
                    total += self.rows[i][k] * other.rows[k][j]
                new_row.append(total)
            result.append(new_row)

        return Matrix(result)

    def __str__(self):
        return "\n".join(str(row) for row in self.rows)


if __name__ == "__main__":
    A = Matrix([[1, 2, 3],
                [4, 5, 6]])

    B = Matrix([[7, 8],
                [9, 10],
                [11, 12]])

    print("A =")
    print(A)
    print("\nB =")
    print(B)
    print("\nA * B =")
    print(A * B)

