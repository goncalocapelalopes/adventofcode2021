PUZZLE_INPUT_FILE = "puzzle_input.txt"


def get_surrounding(i, j, matrix):
    res = []
    rows = len(matrix)
    cols = len(matrix[0])

    if i > 0:
        res.append(matrix[i-1][j])
    if i < rows - 1:
        res.append(matrix[i+1][j])

    if j > 0:
        res.append(matrix[i][j-1])
    if j < cols-1:
        res.append(matrix[i][j+1])
    res.append(matrix[i][j])
    return res


if __name__ == "__main__":
    height_map = open(PUZZLE_INPUT_FILE, "r").readlines()
    height_map = [list(line.strip()) for line in height_map]
    sum_risk = 0
    for i in range(len(height_map)):
        for j in range(len(height_map[i])):
            surroundings = get_surrounding(i, j, height_map)
            lowest = min(surroundings)
            if (height_map[i][j] == lowest) and (surroundings.count(lowest) == 1):
                sum_risk += int(height_map[i][j]) + 1

    print(sum_risk)
