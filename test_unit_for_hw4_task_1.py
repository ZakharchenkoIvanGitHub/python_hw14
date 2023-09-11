from hw4_task_1 import transport_matrix, transport_matrix_zip
import unittest


class TestCaseName(unittest.TestCase):
    def test_method(self):
        self.assertEqual(transport_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]]),
                         [[1, 5, 9], [2, 6, 0], [3, 7, 1], [4, 8, 2]])

        self.assertEqual(transport_matrix_zip([[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]]),
                         [(1, 5, 9), (2, 6, 0), (3, 7, 1), (4, 8, 2)])

        self.assertRaises(IndexError, transport_matrix, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0]])

        self.assertRaises(TypeError, transport_matrix_zip, 55)


if __name__ == '__main__':
    unittest.main(verbosity=2)
