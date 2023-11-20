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
total_fuel = 0
for mass in cleaned_data:
    fuel = (mass // 3) -2
    total_fuel += fuel

# Method 2 - more "pythonic"
total_fuel_2 = sum((mass // 3) - 2 for mass in cleaned_data)

# The code gives the right answer according to the website
# TODO: Design some unit tests for this to make sure it's right
# TODO: Write a pre-commit hook to run the tests