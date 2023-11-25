"""
day_5_code
"""

# I don't want to reuse the code from before, as it will almost certainly have to be rewritten.
# Here are all the program rules

"""
Opcode 1 adds together numbers read from two positions and stores the result in a third position. The three integers immediately after the opcode tell you these three positions - the first two indicate the positions from which you should read the input values, and the third indicates the position at which the output should be stored.

Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them. Again, the three integers after the opcode indicate where the inputs and outputs are, not their values.

Opcode 3 takes a single integer as input and saves it to the position given by its only parameter. For example, the instruction 3,50 would take an input value and store it at address 50.

Opcode 4 outputs the value of its only parameter. For example, the instruction 4,50 would output the value at address 50.

Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.

Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.

Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.

Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.

Right now, your ship computer already understands parameter mode 0, position mode, which causes the parameter to be interpreted as a position - if the parameter is 50, its value is the value stored at address 50 in memory. Until now, all parameters have been in position mode.

Now, your ship computer will also need to handle parameters in mode 1, immediate mode. In immediate mode, a parameter is interpreted as a value - if the parameter is 50, its value is simply 50.

The TEST diagnostic program will start by requesting from the user the ID of the system to test by running an input instruction - provide it 1, the ID for the ship's air conditioner unit.

It will then perform a series of diagnostic tests confirming that various parts of the Intcode computer, like parameter modes, function correctly. For each test, it will run an output instruction indicating how far the result of the test was from the expected value, where 0 means the test was successful. Non-zero outputs mean that a function is not working correctly; check the instructions that were run before the output instruction to see which one failed.

Finally, the program will output a diagnostic code and immediately halt. This final output isn't an error; an output followed immediately by a halt means the program finished. If all outputs were zero except the diagnostic code, the diagnostic program ran successfully.

After providing 1 to the only input instruction and passing all the tests, what diagnostic code does the program produce?
"""
import sys

class computer:
    def __init__(self, program, input_):
        self.program = program
        self.input = input_

    def get_param(self, mode, value):
        if mode == "0":
            return self.program[value]
        else:
            return value

    def compute(self):
        pointer = 0
        while True:
            inst = self.program[pointer]
            opcode = inst % 100
            mode3, mode2, mode1 = f"{inst // 100:03d}"
            assert mode3 == "0"
            if opcode == 1:
                self.program[self.program[pointer + 3]] = self.get_param(
                    mode1, self.program[pointer + 1]
                ) + self.get_param(mode2, self.program[pointer + 2])
                pointer += 4
            elif opcode == 2:
                self.program[self.program[pointer + 3]] = self.get_param(
                    mode1, self.program[pointer + 1]
                ) * self.get_param(mode2, self.program[pointer + 2])
                pointer += 4
            elif opcode == 3:
                self.program[self.program[pointer + 1]] = self.input
                pointer += 2
            elif opcode == 4:
                print(f"{self.program[self.program[pointer+1]]}")
                pointer += 2
            elif opcode == 5:
                if self.get_param(mode1, self.program[pointer + 1]) != 0:
                    pointer = self.get_param(mode2, self.program[pointer + 2])
                else:
                    pointer += 3
            elif opcode == 6:
                if self.get_param(mode1, self.program[pointer + 1]) == 0:
                    pointer = self.get_param(mode2, self.program[pointer + 2])
                else:
                    pointer += 3
            elif opcode == 7:
                self.program[self.program[pointer+3]] = int(self.get_param(mode1, self.program[pointer + 1]) < self.get_param(mode2, self.program[pointer + 2]))
                pointer += 4
            elif opcode == 8:
                self.program[self.program[pointer+3]] = int(self.get_param(mode1, self.program[pointer + 1]) == self.get_param(mode2, self.program[pointer + 2]))
                pointer += 4
            elif opcode == 99:
                break
            else:
                print("Error")
                sys.exit()
    
file_path = "day_5/"
question_file = "day_5_input.txt"

with open(file_path + question_file) as f:
    lines = f.readlines()

diagnostic_code = [int(line) for line in lines[0].split(",")]

comp = computer(diagnostic_code, 5)
comp.compute()