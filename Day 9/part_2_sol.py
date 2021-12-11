PUZZLE_INPUT_FILE = "puzzle_input.txt"


def get_basin(i, j, matrix, curr_basin):
    surr = get_surrounding(i, j, matrix)
    if len(set(curr_basin + surr)) == len(curr_basin):
        return curr_basin
    else:
        for xy in surr:
            if (xy[0], xy[1]) not in curr_basin:
                curr_basin.append((xy[0], xy[1]))
                curr_basin = list(set(curr_basin + get_basin(xy[0], xy[1], matrix, curr_basin)))
        return curr_basin


def get_surrounding(i, j, matrix):
    res = []
    rows = len(matrix)
    cols = len(matrix[0])

    if i > 0 and int(matrix[i-1][j]) < 9:
        res.append((i-1, j))
    if i < rows - 1 and int(matrix[i+1][j]) < 9:
        res.append((i+1, j))

    if j > 0 and int(matrix[i][j-1]) < 9:
        res.append((i, j-1))
    if j < cols-1 and int(matrix[i][j+1]) < 9:
        res.append((i, j+1))
    res.append((i, j))
    return res


if __name__ == "__main__":
    height_map = open(PUZZLE_INPUT_FILE, "r").readlines()

    height_map = [list(line.strip()) for line in height_map]
    basin_sizes = []
    for i in range(len(height_map)):
        for j in range(len(height_map[i])):
            if height_map[i][j] == "9":
                continue
            surroundings = get_surrounding(i, j, height_map)
            surroundings = [int(height_map[xy[0]][xy[1]]) for xy in surroundings]
            lowest = min(surroundings)
            if (int(height_map[i][j]) == lowest) and (surroundings.count(lowest) == 1):
                basin_sizes.append(len(get_basin(i, j, height_map, [(i, j)])))

    basin_sizes = sorted(basin_sizes)
    print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])
