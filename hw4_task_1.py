"""Напишите функцию для транспонирования матрицы"""
import doctest


def print_matrix(matrix: list):
    for el in matrix:
        print(*el)


def transport_matrix(matrix: list) -> list:
    """
    функция для транспонирования матрицы
    >>>  transport_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]])
    [[1, 5, 9], [2, 6, 0], [3, 7, 1], [4, 8, 2]]
    """
    rows = len(matrix)
    columns = len(matrix[0])
    new_matrix = [[0 for _ in range(rows)] for _ in range(columns)]
    for ind1 in range(rows):
        for ind2 in range(columns):
            new_matrix[ind2][ind1] = matrix[ind1][ind2]
    return new_matrix


def transport_matrix_zip(matrix: list) -> list:
    """
    функция для транспонирования матрицы
    >>>  transport_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]])
    [[1, 5, 9], [2, 6, 0], [3, 7, 1], [4, 8, 2]]
    """
    return list(zip(*matrix))


if __name__ == '__main__':
    print(transport_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]]))
    doctest.testmod(verbose=True)
