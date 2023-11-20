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
# TODO: Write a pre-commit hook to run the tests
"""
What is the sum of the fuel requirements for all of the modules on your spacecraft when also taking into account the mass of the added fuel?

(Calculate the fuel requirements for each module separately, then add them all up at the end.)

"""
# First, make anything less than zero =  0
def single_fuel(mass):
    fuel = (mass // 3) -2
    if fuel > 0:
        return fuel
    else:
        return 0

# Calculate the total fuel requirement for one module
def fuel_for_fuel(weight):
    total = 0
    new_fuel = single_fuel(weight)
    while new_fuel != 0:
        total += new_fuel
        new_fuel = single_fuel(new_fuel)
    return total

spaceship_total = 0
for weight in cleaned_data:
    spaceship_total += fuel_for_fuel(weight)
print(spaceship_total)
