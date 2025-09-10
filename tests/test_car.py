import pytest
from unittest.mock import patch

from my_module import Car


@pytest.fixture
def car() -> Car:
    return Car(made="Mazda", model="MC5", year="1916", engine_volume=95.5, fuel_efficiency=30)


def test_car_str_representation(car):
    assert car.__str__() == "Автомобіль: 1916 Mazda 30."


def test_car_repr(car: Car):
    assert car.__repr__() == 'Car(made="Mazda", model="MC5", year="1916", engine_volume=95.5, fuel_efficiency=30)'


def test_car_eq(car: Car):
    assert car == car


@pytest.mark.parametrize("distance,consumption", [
    (1, 0.3),
    (100, 30),
    (15, 4.5)
])
def test_calculate_fuel_consumption(car: Car, distance, consumption):
    assert car.calculate_fuel_consumption(distance) == consumption


@pytest.mark.parametrize("gear", ['D', 'R', 'P', 'N', 1, 2, 3, 4, 5])
def test_shift_gear(car, gear):
    assert car.shift_gear(gear) == f'Перемикаємо передачу на: {gear}'