PUZZLE_INPUT_FILE = "puzzle_input.txt"
from statistics import median

def fuel_spent(pos_start, pos_end):
    return abs(pos_start - pos_end)


if __name__ == "__main__":
    positions = open(PUZZLE_INPUT_FILE, "r").readline().split(",")
    positions = [int(p) for p in positions]

    best_pos = median(positions)
    fuel = sum([fuel_spent(pos_start, best_pos) for pos_start in positions])
    print(fuel)
