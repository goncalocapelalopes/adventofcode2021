import numpy as np

MIN_SIZE = -50
MAX_SIZE = 50

INFILE = "puzzle.txt"

def map_coord(in_coord):
    if in_coord < MIN_SIZE:
        return 0
    elif in_coord > MAX_SIZE:
        return 99
    else:
        return min(in_coord + 49, 99)

def update_grid(grid, cuboid, signal):
    """
        grid --> np.array of shape (MAX_SIZE + 50, MAX_SIZE + 50, MAX_SIZE + 50)
        cuboid --> list of 3 pairs, [[x_start, x_end], [y_start, y_end], [z_start, z_end]]
        signal --> 0 to turn off, 1 to turn on
    """
    x_start, x_end = cuboid[0]
    y_start, y_end = cuboid[1]
    z_start, z_end = cuboid[2]
    
    for x in range(x_start, x_end+1):
        for y in range(y_start, y_end+1):
            for z in range(z_start, z_end+1):
                grid[x][y][z] = signal
    return grid

def count_ons(grid):
    return np.sum(grid, axis=None)

def parse_line(line):
    signal, cuboid_str = line.split(" ")
    cuboid = []
    for substr in cuboid_str.split(","):
        substr = substr.split("=")[-1]
        start, end = [int(c) for c in substr.split("..")]
        if start < MIN_SIZE or end > MAX_SIZE:
            raise ValueError("Out of range.")

        start = map_coord(start)
        end = map_coord(end)
        cuboid.append((start, end))
    
    signal = int(signal=="on")
    return cuboid, signal

if __name__ == "__main__":
    grid = np.zeros((100, 100, 100))
    lines = open(INFILE, "r").readlines()
    
    instrs = []
    for line in lines:
        try:
            cuboid, signal = parse_line(line)
        except ValueError as e:
            print(e)
            continue
        print(cuboid, signal)
        grid = update_grid(grid, cuboid, signal)

    print(count_ons(grid))

    









