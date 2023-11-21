"""
Read in data from the .txt
"""
file_path = "day_6/"
question_file = "day_6_input.txt"

with open(file_path + question_file) as f:
    lines = f.readlines()
"""
Clean the data to get rid of \n
"""
coords = [line.replace("\n", "") for line in lines]
"""
What is the total number of direct and indirect orbits in your map data?
"""
def direct_orbits(coordinates):
    """
    Takes a list of orbiting pairs and calculates which planets are orbiting eachother.

    Parameters
    ----------
        coordinates : list[str]
    A list of strings with the format center_planet)orbiting_planet

    Returns
    --------
        direct_orbit_dict: dict{center_planet: [orbiting_planet_1, orbiting_planet_2]}
    A dictionary where the keys are strings (center_planet) and the values are a list of strings of orbiters.
    """
    direct_orbit_dict = {}
    for pair in coordinates:
        center, orbiter = pair.split(")")
        direct_orbit_dict.setdefault(center, []).append(orbiter)
    return direct_orbit_dict

def indirect_orbits(direct_orbit_dict):
    """
    Groups planets by distance from COM.

    Parameters
    ----------
        direct_orbit_dict: dict{center_planet: [orbiting_planet_1, orbiting_planet_2]}
    A dictionary where the keys are strings (center_planet) and the values are a list of strings of orbiters.

    Returns
    --------
        distance_from_com: dict {int: list[str]}  
    A dictionary with keys (ints) as distance from COM and a list of planet names at that distance.
    """
    distance_from_com = {0: ["COM"]}
    x = 0
    while x in distance_from_com.keys():
        new_centers = distance_from_com[x]
        for center in new_centers:
            orbiters = direct_orbit_dict.get(center, [])
            distance_from_com.setdefault(x + 1, []).extend(orbiters)
        x += 1
    return distance_from_com

def sum_orbits(coordinates):
    """
    Returns the total number of orbits within the system
    
    Parameters
    -----------
        coordinates : list[str]
    A list of strings with the format center_planet)orbiting_planet

    Returns
    ---------
        total_orbits : int
    The sum of the orbits (direct and indirect)
    """
    layers = indirect_orbits(direct_orbits(coordinates))
    total_orbits = sum(key * len(layers[key]) for key in layers.keys())
    return total_orbits

# Part 1 OK
"""
What is the minimum number of orbital transfers required to move from the object YOU are orbiting to the object SAN is orbiting? (Between the objects they are orbiting - not between YOU and SAN.)
"""
# We want to find the closest common orbiter
# Then it's just the distance up from that to YOU and SAN

def route_to_com(orbit_list, start_point):
    route = [start_point]
    # Assuming nobody is orbiting around me and / or sam
    while "COM" not in route:
        for key in orbit_list.keys():
            if start_point in orbit_list[key]:
                route.append(key)
                start_point = key
    return route
                

san_route = route_to_com(direct_orbits(coords), "SAN")
you_route = route_to_com(direct_orbits(coords), "YOU")

def closet_commom_orbit(route_1, route_2):
    for position in route_2:
        if position in route_1:
            common = position
            print(common)
            distance = route_1.index(common) + route_2.index(common) -2 # We have to -2 because it is the distance from the objects we are orbiting, not to eachother.
            return distance

print(closet_commom_orbit(san_route, you_route))
