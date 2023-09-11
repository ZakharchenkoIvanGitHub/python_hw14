import pytest
from hw4_task_1 import transport_matrix, transport_matrix_zip


def test_access():
    assert transport_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]]) == \
           [[1, 5, 9], [2, 6, 0], [3, 7, 1], [4, 8, 2]], "Ошибка транспонирования матрицы"

    assert transport_matrix_zip([[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]]) == \
           [(1, 5, 9), (2, 6, 0), (3, 7, 1), (4, 8, 2)], "Ошибка транспонирования матрицы"


def test_exception():
    with pytest.raises(IndexError):
        transport_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 0]])

    with pytest.raises(TypeError):
        transport_matrix_zip(55)


if __name__ == '__main__':
    pytest.main(['-v'])
