import unittest
from vehicle import Vehicle, Car, Motorcycle


class TestVehicles(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car('Lotus', 'Evora', 2009)
        self.bike = Motorcycle('Yamaha', 'Jupiter Z1', 2023)

    def test_car_is_vehicle(self):
        self.assertTrue(isinstance(self.car, Vehicle))

    def test_car_has_4_wheels(self):
        self.assertEqual(self.car.wheels_num, 4)

    def test_car_test_drive_speed(self):
        self.car.test_drive()
        self.assertEqual(self.car.speed, 60)

    def test_car_park_speed(self):
        self.car.test_drive()
        self.car.park()
        self.assertEqual(self.car.speed, 0)

    def test_bike_has_2_wheels(self):
        self.assertEqual(self.bike.wheels_num, 2)

    def test_bike_test_drive_speed(self):
        self.bike.test_drive()
        self.assertEqual(self.bike.speed, 75)

    def test_bike_park_speed(self):
        self.bike.test_drive()
        self.bike.park()
        self.assertEqual(self.bike.speed, 0)
