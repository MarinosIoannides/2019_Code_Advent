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
# Day 3
from day_3.day_3_code import closest_crossover, shortest_crossover
@pytest.mark.parametrize(
    "wire_1, wire_2, expected_output",
    [
        (
            ["R75","D30","R83","U83","L12","D49","R71","U7","L72"], 
            ["U62","R66","U55","R34","D71","R55","D58","R83"], 
            159,
        ),
        (
            ["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"],
            ["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"],
            135,
        )
    ]
)
def test_closest_crossover(wire_1, wire_2 , expected_output):
    calculation = closest_crossover(wire_1, wire_2)
    assert calculation == expected_output
@pytest.mark.parametrize(
    "wire_1, wire_2, expected_output",
    [
        (
            ["R75","D30","R83","U83","L12","D49","R71","U7","L72"], 
            ["U62","R66","U55","R34","D71","R55","D58","R83"], 
            610,
        ),
        (
            ["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"],
            ["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"],
            410,
        )
    ]
)
def test_shortest_crossover(wire_1, wire_2 , expected_output):
    calculation = shortest_crossover(wire_1, wire_2)
    assert calculation == expected_output

# Day 4

from day_4.day_4_code import find_pair
@pytest.mark.parametrize(
    "number_list, has_pair",
    [
        (
            ["1", "1", "1", "2", "3"],
            False
        ),
        (
            ["1", "1", "2", "3", "3"],
            True
        ),
        (
            ["2", "1", "2", "4", "3"],
            True
        )
    ]
)
def test_find_pair(number_list, has_pair):
    calculation = find_pair(number_list)
    assert calculation == has_pair

# Day 6
from day_6.day_6_code import sum_orbits, from_san_to_me
@pytest.mark.parametrize(
    "orbit_list, total_orbits",
    [
        (
            ["COM)B", "B)C", "C)D", "D)E",
            "E)F", "B)G", "G)H", "D)I", "E)J",
            "J)K", "K)L"],
            42
        )
    ]
)
def test_sum_orbits(orbit_list, total_orbits):
    calculation = sum_orbits(orbit_list)
    assert calculation == total_orbits

@pytest.mark.parametrize(
    "orbit_list, total_jumps",
    [
        (
            ["COM)B", "B)C", "C)D", "D)E", "E)F",
            "B)G",  "G)H", "D)I", "E)J", "J)K",  "K)L",
            "K)YOU",  "I)SAN"],
            4
        )
    ]
)
def test_jumps(orbit_list, total_jumps):
    calculation = from_san_to_me(orbit_list)
    assert calculation == total_jumps