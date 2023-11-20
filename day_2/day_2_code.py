"""
What value is left at position 0 after the program halts?

1 = Add
2 = Multiply
99 = Stop
Other = Error
"""

"""
Read in data from the .txt
"""
file_path = "day_2/"
question_file = "day_2_input.txt"
with open(file_path + question_file) as f:
    lines = f.readlines()

"""
Clean the data into a list of ints
"""
cleaned_data = [int(line) for line in lines[0].split(",")]
"""
There doesn't seem to be an easy way to test this or to functionalise it
"""
def program_fix_1(input_list):
    working_list = input_list.copy()
    for position in range(0, len(working_list),4):
        decision_code = working_list[position]
        position_1 = working_list[position + 1]
        position_2 = working_list[position + 2]
        location_code = working_list[position + 3]
        placement_number = -1
        if decision_code == 99:
            return working_list[0]
        elif decision_code == 1:
            placement_number = working_list[position_1] + working_list[position_2]
        elif decision_code == 2:
            placement_number = working_list[position_1] * working_list[position_2]
        else:
            return("Invalid code")
        working_list[location_code] = placement_number

print(program_fix_1(cleaned_data))

"""
"With terminology out of the way, we're ready to proceed. To complete the gravity assist, you need to determine what pair of inputs produces the output 19690720."

The inputs should still be provided to the program by replacing the values at addresses 1 and 2, just like before. In this program, the value placed in address 1 is called the noun, and the value placed in address 2 is called the verb. Each of the two input values will be between 0 and 99, inclusive.
Find the input noun and verb that cause the program to produce the output 19690720. What is 100 * noun + verb? (For example, if noun=12 and verb=2, the answer would be 1202.)
"""
# Attempt 1 - Is there a pattern
# Answer - No clear pattern from incrementing verb / noun
answer = 19690720
# Attempt 2 - How do we make 19690720?
prime_factors = "2 x 2 x 2 x 2 x 2 x 5 x 7 x 17581"

# Attempt 3: Just try every combination
# This feels like cheating but seems the only way
for n in range(1, 100):
    noun = n
    for v in range(1,100):
        verb = v
        improved_input = cleaned_data
        improved_input[0] = 1
        improved_input[1] = noun
        improved_input[2] = verb
        if program_fix_1(improved_input) == answer:
            print(f"verb = {v}, noun = {n}")
            print(f"Submit {100*noun + verb} to website")

# This gives the right answer! 
# There must be a clever way of doing it...