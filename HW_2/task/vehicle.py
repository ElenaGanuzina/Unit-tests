from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, company: str, model: str, release_year: int,
                 wheels_num: int, speed: int):
        self._company = company
        self._model = model
        self._release_year = release_year
        self._wheels_num = wheels_num
        self._speed = speed

    @property
    def company(self):
        return self._company

    @property
    def model(self):
        return self._model

    @property
    def release_year(self):
        return self._release_year

    @property
    def wheels_num(self):
        return self._wheels_num

    @property
    def speed(self):
        return self._speed

    @abstractmethod
    def test_drive(self):
        pass

    @abstractmethod
    def park(self):
        pass


class Car(Vehicle):

    def __init__(self, company: str, model: str, release_year: int):
        super().__init__(company, model, release_year, wheels_num=4, speed=0)

    def test_drive(self):
        self._speed = 60

    def park(self):
        self._speed = 0

    def __repr__(self):
        return f'Car {self._company} {self._model}, release year {self._release_year}'


class Motorcycle(Vehicle):

    def __init__(self, company: str, model: str, release_year: int):
        super().__init__(company, model, release_year, wheels_num=2, speed=0)

    def test_drive(self):
        self._speed = 75

    def park(self):
        self._speed = 0

    def __repr__(self):
        return f'Motorcycle {self._company} {self._model}, release year {self._release_year}'
