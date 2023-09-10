"""
Создайте класс Матрица. Добавьте методы для: - вывода на печать,
сравнения, сложения, умножения матриц
"""


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def __str__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.data == other.data
        else:
            return False

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.rows == other.rows and self.cols == other.cols:
                result = Matrix(self.rows, self.cols)
                for i in range(self.rows):
                    for j in range(self.cols):
                        result.data[i][j] = self.data[i][j] + other.data[i][j]
                return result
            else:
                raise ValueError("Матрицы должны иметь одинаковое количество строк и столбцов")
        else:
            raise ValueError("Второй объект не матрица")

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.cols == other.rows:
                result = Matrix(self.rows, other.cols)
                for i in range(self.rows):
                    for j in range(other.cols):
                        dot_product = 0
                        for k in range(self.cols):
                            dot_product += self.data[i][k] * other.data[k][j]
                        result.data[i][j] = dot_product
                return result
            else:
                raise ValueError("Число столбцов первой матрицы должно быть равно числу строк второй матрицы")
        else:
            raise ValueError("Второй объект не матрица")