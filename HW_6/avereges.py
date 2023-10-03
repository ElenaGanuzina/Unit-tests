from typing import List, Tuple


class Average:
    def __init__(self, lst_1: List[int], lst_2: List[int]):
        self._lst_1 = lst_1
        self._lst_2 = lst_2

    @property
    def lst_1(self):
        return self._lst_1

    @property
    def lst_2(self):
        return self._lst_2

    def find_averages(self) -> Tuple[float, float]:
        if len(self._lst_1):
            average_1 = sum(self._lst_1) / len(self._lst_1)
        else:
            average_1 = 0
        if len(self._lst_2):
            average_2 = sum(self._lst_2) / len(self._lst_2)
        else:
            average_2 =0
        return average_1, average_2

    def compare_averages(self) -> None:
        average_1, average_2 = self.find_averages()
        if average_1 == average_2:
            print('Средние значения равны')
        elif average_1 > average_2:
            print('Первый список имеет большее среднее значение')
        else:
            print('Второй список имеет большее среднее значение')



