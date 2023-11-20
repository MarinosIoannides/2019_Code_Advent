"""
advent_tests.py
---------
By turning the questions into unit tests, it helps our understanding and makes our code more RAP
"""
import pytest

# On the first day of Xmas...
from day_1.day_1_code import total_fuel_loop, total_fuel_pythonic
@pytest.mark.parametrize(
    "data_list, expected_output",
    [
        ([100, 100, 100], 93),
        ([ 21,  22,  23], 15),
    ]
)
def test_loop(data_list, expected_output):
    calculation = total_fuel_loop(data_list)
    calculation_2 = total_fuel_pythonic(data_list)
    assert calculation == expected_output and calculation_2 == expected_output