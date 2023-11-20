"""
Read in data from the .txt
"""
file_path = "day_1/"
question_file = "day_1_input.txt"
with open(file_path + question_file) as f:
    lines = f.readlines()
"""
Clean the data into a list of ints
"""
cleaned_data = [int(line) for line in lines]
"""
To find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.
"""
# Method 1 - Looping through list
def total_fuel_loop(list_of_weights):
    total_fuel = 0
    for mass in list_of_weights:
        fuel = (mass // 3) -2
        total_fuel += fuel
    return total_fuel

# Method 2 - more "pythonic"
def total_fuel_pythonic(list_of_weights):
    return sum((mass // 3) - 2 for mass in list_of_weights)

# The code gives the right answer according to the website
# TODO: Design some unit tests for this to make sure it's right
# TODO: Write a pre-commit hook to run the tests