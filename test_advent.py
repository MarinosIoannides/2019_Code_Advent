"""
advent_tests.py
---------
By turning the questions into unit tests, it helps our understanding and makes our code more RAP
"""
import pytest

# On the first day of Xmas...
from day_1.day_1_code import total_fuel_loop, total_fuel_pythonic, single_fuel, fuel_for_fuel

@pytest.mark.parametrize(
    "data_list, expected_output",
    [
        ([100, 100, 100], 93),
        ([ 21,  22,  23], 15),
    ]
)
def test_basic(data_list, expected_output):
    calculation = total_fuel_loop(data_list)
    calculation_2 = total_fuel_pythonic(data_list)
    assert calculation == expected_output and calculation_2 == expected_output

@pytest.mark.parametrize(
    "input, expected_output",
    [
        (0, 0),
        (-100, 0),
        (10, 1),
    ]
)
def test_indiv_calc(input, expected_output):
    calculation = single_fuel(input)
    assert calculation == expected_output

@pytest.mark.parametrize(
    "input, expected_output",
    [
        (0, 0),
        (-100, 0),
        (10, 1),
        (33, 10)
    ]
)
def test_fuel_for_fuel(input, expected_output):
    calculation = fuel_for_fuel(input)
    assert calculation == expected_output