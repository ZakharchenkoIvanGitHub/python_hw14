from matrix import Matrix
import io
import unittest
from unittest.mock import patch


class TestSample(unittest.TestCase):
    def setUp(self) -> None:
        self.m1 = Matrix(2, 2)
        self.m1.data = [[1, 2], [3, 4]]

        self.m2 = Matrix(2, 2)
        self.m2.data = [[6, 8], [10, 12]]

        self.m3 = Matrix(2, 2)
        self.m3.data = [[5, 6], [7, 8]]

        self.m4 = Matrix(2, 2)
        self.m4.data = [[19, 22], [43, 50]]

        self.m5 = Matrix(2, 2)
        self.m5.data = [[1, 2], [3, 4]]

        self.m6 = Matrix(3, 3)
        self.m6.data = [[1, 2], [3, 4], [5, 6]]

    def test_add(self):
        self.assertEqual(self.m1 + self.m3, self.m2)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print(self, mock_stdout):
        print(self.m1)
        self.assertEqual(mock_stdout.getvalue(), "1 2\n3 4\n\n")

    def test_mul(self):
        self.assertEqual(self.m1 * self.m3, self.m4)

    def test_eq(self):
        self.assertTrue(self.m1 == self.m5)
        self.assertTrue(self.m1 != self.m2)
        self.assertFalse(self.m1 == self.m2)
        self.assertFalse(self.m1 != self.m5)

    def test_raises(self):
        self.assertRaisesRegex(ValueError, "Матрицы должны иметь одинаковое количество строк и столбцов",
                               Matrix.__add__, self.m1, self.m6)

        self.assertRaisesRegex(ValueError, "Второй объект не матрица", Matrix.__add__, self.m1, 5)

        self.assertRaisesRegex(ValueError, "Число столбцов первой матрицы должно быть равно числу строк второй матрицы",
                               Matrix.__mul__, self.m1, self.m6)

        self.assertRaisesRegex(ValueError, "Второй объект не матрица", Matrix.__mul__, self.m1, 5)


if __name__ == '__main__':
    unittest.main(verbosity=2)
