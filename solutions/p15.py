import math

def step_count(lattice_size):
    fact = math.factorial(lattice_size)
    return math.factorial(2 * lattice_size) / fact / fact


print(step_count(20))