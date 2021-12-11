PUZZLE_INPUT_FILE = "puzzle_input.txt"
STEPS = 100


def get_surrounding(i, j, matrix):
    res = []
    rows = len(matrix)
    cols = len(matrix[0])

    if i > 0:
        res.append((i-1, j))
        if j > 0:
            res.append((i-1, j-1))
        if j < cols-1:
            res.append((i-1, j+1))
    if i < rows - 1:
        res.append((i+1, j))
        if j > 0:
            res.append((i+1, j-1))
        if j < cols-1:
            res.append((i+1, j+1))
    if j > 0:
        res.append((i, j-1))
    if j < cols-1:
        res.append((i, j+1))
    return res


def create_zeros_matrix(rows, cols):
    return [[0] * cols for _ in range(rows)]


def update_matrix(i, j, matrix, flashed_matrix):

    if matrix[i][j] == 9:
        matrix[i][j] = 0
        flashed_matrix[i][j] = 1
        surr = get_surrounding(i, j, matrix)
        for x, y in surr:
            if flashed_matrix[x][y] == 0:
                matrix, flashed_matrix = update_matrix(x, y, matrix, flashed_matrix)
            elif matrix[x][y] == 0 and flashed_matrix[x][y] == 0:
                matrix[x][y] += 1
    else:
        if flashed_matrix[i][j] == 0:
            matrix[i][j] += 1
    return matrix, flashed_matrix


if __name__ == "__main__":
    matrix = open(PUZZLE_INPUT_FILE, "r").read().splitlines()
    matrix = [list(map(int, list(line))) for line in matrix]

    n_flashes = 0

    for _ in range(STEPS):
        flashed_matrix = create_zeros_matrix(len(matrix), len(matrix[0]))
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix, flashed_matrix = update_matrix(i, j, matrix, flashed_matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                n_flashes += ((matrix[i][j]) == 0) * 1

    print(n_flashes)
