PUZZLE_INPUT_FILE = "puzzle_input_extra.txt"
from statistics import mean, median
import math

def cumulative_fuel(steps):
    print(steps)
    if steps <= 1:
        return steps
    else:
        return steps + cumulative_fuel(steps-1)

def cumulative_fuel2(steps):
    cumfuel = 0
    for i in range(steps+1):
        cumfuel += i
    return cumfuel

def fuel_spent(pos_start, pos_end):
    return cumulative_fuel2(abs(pos_start - pos_end))

def total_fuel_spent(positions, pos_end):
    return sum([fuel_spent(pos, pos_end) for pos in positions])

if __name__ == "__main__":
    positions = open(PUZZLE_INPUT_FILE, "r").readline().split(",")
    positions = sorted([int(p) for p in positions])

    best_pos_0 = median(positions)

    # search right
    best_pos = -1
    curr_best_fuel = float("inf")

    for pos in range(best_pos_0, positions[-1]):
        curr_fuel = total_fuel_spent(positions, pos)
        if curr_fuel < curr_best_fuel:
            curr_best_fuel = curr_fuel
            best_pos = pos
        else:
            break
    # search left
    for pos in range(best_pos_0, positions[0], -1):
        curr_fuel = total_fuel_spent(positions, pos)
        if curr_fuel < curr_best_fuel:
            curr_best_fuel = curr_fuel
            best_pos = pos
        else:
            break

    print(best_pos)
    print(curr_best_fuel)
