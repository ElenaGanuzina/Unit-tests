import pytest

from avereges import Average


@pytest.fixture
def set_up():
    lst_1 = [1, 2, 3, 4, 5]
    lst_2 = [9, 8, 7, 6, 5]
    return lst_1, lst_2


def test_create_average(set_up):
    """Проверка создания экземплра класса Average."""
    lst_1, lst_2 = set_up
    avg = Average(lst_1, lst_2)
    assert avg.lst_1 == lst_1, 'test_create_average failed: incorrect lst_1'
    assert avg.lst_2 == lst_2, 'test_create_average failed: incorrect lst_2'


def test_find_averages(set_up):
    """Проверка корректоного нахождения средних значений, списки имеют длину > 1."""
    lst_1, lst_2 = set_up
    avg = Average(lst_1, lst_2)
    assert avg.find_averages() == (3.0, 7.0), 'test_find_averages failed'


@pytest.mark.parametrize('lst_1, lst_2, result', [
    ([2], [1, 2, 3], (2.0, 2.0)),
    ([1, 2, 3], [1], (2.0, 1.0)),
    ([3], [2], (3.0, 2.0))
])
def test_find_avg_one_item(lst_1, lst_2, result):
    """Проверка корректного нахождения средних значений, один или оба списка содержат 1 элемент."""
    avg = Average(lst_1, lst_2)
    assert avg.find_averages() == result, 'test_find_avg_one_item failed'


@pytest.mark.parametrize('lst_1, lst_2, result', [
    ([], [1, 2, 3], (0, 2.0)),
    ([1, 2, 3], [], (2.0, 0)),
    ([], [], (0, 0))
])
def test_find_avg_empty_list(lst_1, lst_2, result):
    """Проверка корректного нахождения средних значений, один или оба списка пустые."""
    avg = Average(lst_1, lst_2)
    assert avg.find_averages() == result, 'test_find_avg_empty_list failed'


def test_compare_avgs_first_greater(set_up, capfd):
    """Проверка сравнения средних значений, первое больше."""
    lst_2, lst_1 = set_up
    avg = Average(lst_1, lst_2)
    avg.compare_averages()
    out, err = capfd.readouterr()
    assert out.strip() == 'Первый список имеет большее среднее значение', 'test_compare_avgs_first_greater failed'


def test_compare_avgs_second_greater(set_up, capfd):
    """Проверка сравнения средних значений, второе больше."""
    lst_1, lst_2 = set_up
    avg = Average(lst_1, lst_2)
    avg.compare_averages()
    out, err = capfd.readouterr()
    assert out.strip() == 'Второй список имеет большее среднее значение', 'test_compare_avgs_second_greater failed'


def test_compare_avgs_equal(set_up, capfd):
    """Проверка сравнения средних значений, значения равны."""
    lst_1, lst_2 = set_up
    lst_2 = lst_1
    avg = Average(lst_1, lst_2)
    avg.compare_averages()
    out, err = capfd.readouterr()
    assert out.strip() == 'Средние значения равны', 'test_compare_avgs_equal failed'
