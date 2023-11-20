"""
day_3_code

Note - this is really fun but I'm sure this isn't the best way of doing it.
"""
file_path = "day_3/"
question_file = "day_3_input.txt"
with open(file_path + question_file) as f:
    lines = f.readlines()
wire_1 = lines[0].split(",")
wire_2 = lines[1].split(",")

start_point = (0,0)
# Right is positive in the x direction
# Up is positive in the y direction

def pathing(wire):
    """
    A function which creates the pattern of the wires from a series of directions

    Parameters
    ----------
        wire : list[str]
    A list of strings which have the format LetterNumber e.g. N20

    Returns
    --------
        wire_path : list[tup(int, int)]
    A list of tuples of pairs of ints which represent the x / y coordinates of the wire's locations, in order from the start point (0,0)
    """
    wire_path = [start_point]
    for direction in wire:
        letter = direction[0]
        distance = int(direction[1:])
        # There must be a neater way of doing this
        if letter == "R":
            for i in range(1, distance+1):
                starting_point = wire_path[-1]
                new_point = (starting_point[0] + 1, starting_point[1])
                wire_path.append(new_point)
        if letter == "L":
            for i in range(1, distance+1):
                starting_point = wire_path[-1]
                new_point = (starting_point[0] - 1, starting_point[1])
                wire_path.append(new_point)
        if letter == "U":
            for i in range(1, distance+1):
                starting_point = wire_path[-1]
                new_point = (starting_point[0], starting_point[1] + 1)
                wire_path.append(new_point)
        if letter == "D":
            for i in range(1, distance+1):
                starting_point = wire_path[-1]
                new_point = (starting_point[0], starting_point[1] - 1)
                wire_path.append(new_point)
    return wire_path

def closest_crossover(wire_1, wire_2):
    one_path = set(pathing(wire_1))
    two_path = set(pathing(wire_2))
    intersections = one_path.intersection(two_path)
    distances = []
    for point in intersections:
        manhattan_distance = abs(point[0]) + abs(point[1])
        if manhattan_distance != 0:
            distances.append(manhattan_distance)

    return min(distances)
# Answer to step 1 - Correct
print(closest_crossover(wire_1, wire_2))

def shortest_crossover(wire_1, wire_2):
    one_path = pathing(wire_1)
    two_path = pathing(wire_2)
    intersections = set(one_path).intersection(set(two_path))
    distances = []
    for point in intersections:
        timing_distance = one_path.index(point) + two_path.index(point)
        if timing_distance != 0:
            distances.append(timing_distance)

    return min(distances)
# Answer to step 2 - Correct
print(shortest_crossover(wire_1, wire_2))