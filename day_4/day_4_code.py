"""
day_4_code
"""
# Input given as a range of numbers
lower_end = 240920
upper_end = 789857

import numpy as np
# Rules
# At least 1 duplicate
# Increasing left to right

def count_possible_passwords(start_number, end_number):
    """
    Counts the number of numbers between start and end that conform to the following rules:
        1) There is at least 1 duplicate digit
        2) A digit is never followed by a smaller digit

    Parameters
    ----------
        start_number: int
    The start point for the range of numbers

        end_number : int
    The end point for the range of numbers

    Returns
    -------
        count : int
    The number of numbers within the range that conform to the above rules.
    """
    count = 0
    for number in range(start_number, end_number):
        listed_number = [int(i) for i in str(number)]
        if sorted(listed_number) == listed_number and len(set(listed_number)) != len(listed_number):
            count +=1 
    return count

print(count_possible_passwords(lower_end, upper_end))

# New rules
# At least one pair exactly
def find_pair(list_of_numbers):
    """
    Given a list of 1 digit numbers, return True if there is an exact pair.
    I.E. 2 matching numbers, not 3 or 4 etc.

    Parameters
    -----------
        list_of_numbers : list[int]
    A list of integers where pair detection is required

    Returns
    --------
        bool
    True if there is a pair, false if there is not
    """
    count_dict = {}
    for int in list_of_numbers:
        count_dict.setdefault(int, 0)
        count_dict[int] += 1
    for value in count_dict.values():
        if value == 2:
            return True
    return False

def count_enhanced_passwords(start_number, end_number):
    count = 0
    for number in range(start_number, end_number):
        listed_number = [int(i) for i in str(number)]
        if sorted(listed_number) == listed_number and len(set(listed_number)) != len(listed_number):
            if find_pair(listed_number):
                count += 1
    return count

print(count_enhanced_passwords(lower_end, upper_end))