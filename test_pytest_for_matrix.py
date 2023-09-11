import pytest
from matrix import Matrix


@pytest.fixture
def m1():
    m = Matrix(2, 2)
    m.data = [[1, 2], [3, 4]]
    return m


@pytest.fixture
def m2():
    m = Matrix(2, 2)
    m.data = [[6, 8], [10, 12]]
    return m


@pytest.fixture
def m3():
    m = Matrix(2, 2)
    m.data = [[5, 6], [7, 8]]
    return m


@pytest.fixture
def m4():
    m = Matrix(2, 2)
    m.data = [[19, 22], [43, 50]]
    return m


@pytest.fixture
def m5():
    m = Matrix(2, 2)
    m.data = [[1, 2], [3, 4]]
    return m


@pytest.fixture
def m6():
    m = Matrix(3, 3)
    m.data = [[1, 2], [3, 4], [5, 6]]
    return m


def test_add(m1, m2, m3):
    assert m1 + m3 == m2, "Ошибка сложения"


def test_mlt(m1, m3, m4):
    assert m1 * m3 == m4, "Ошибка умножения"


def test_eq(m1, m2, m5):
    assert m1 == m5, "Ошибка сравнения"
    assert m1 != m2, "Ошибка сравнения"


def test_exception(m1, m6):
    with pytest.raises(ValueError):
        m1 + m6
        m1 + 5
        m1 * m6
        m1 * 5


def test_print(capsys, m1):
    print(m1)
    assert capsys.readouterr().out.strip() == "1 2\n3 4"


if __name__ == '__main__':
    pytest.main(['-v'])
