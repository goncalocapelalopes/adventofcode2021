PUZZLE_INPUT_FILE = "puzzle_input.txt"


def read_puzzle(puzzle_str):
    split_res = puzzle_str.split("\n\n")
    draw_nrs, boards = split_res[0].split(","), split_res[1:]
    boards = [board.split("\n") for board in boards]
    boards = [[row.strip().split() for row in board] for board in boards]

    return draw_nrs, boards


def board_is_complete(board_bool):
    # check rows

    for row in board_bool:
        if sum(row) == len(row):
            return True
    # check columns
    for col in [get_column(board_bool, i) for i in range(len(board_bool[0]))]:
        if sum(col) == len(col):
            return True
    return False


def board_sum_unmarkeds(board, board_bool):
    unmarked_sum = 0
    for row_i in range(len(board_bool)):
        for col_i in range(len(board_bool[row_i])):
            if board_bool[row_i][col_i] == 0:
                unmarked_sum += int(board[row_i][col_i])
    return unmarked_sum


def board_update(board, board_bool, nr):
    for row_i in range(len(board_bool)):
        for col_i in range(len(board_bool[row_i])):
            if board[row_i][col_i] == nr:
                board_bool[row_i][col_i] = 1
    return board_bool


def create_zeros_board(rows, cols):
    return [[0] * cols for _ in range(rows)]


def get_column(board, i):
    return [row[i] for row in board]


if __name__ == "__main__":
    draw_nrs, boards = read_puzzle(open(PUZZLE_INPUT_FILE, "r").read())

    # boards have all the same shape
    board_rows = len(boards[0])
    board_cols = len(boards[0][0])

    boards_bool = [create_zeros_board(board_rows, board_cols) for _ in range(len(boards))]

    for nr in draw_nrs:
        for i in range(len(boards)):
            boards_bool[i] = board_update(boards[i], boards_bool[i], nr)

            if board_is_complete(boards_bool[i]):
                sum_unmarked = board_sum_unmarkeds(boards[i], boards_bool[i])
                print(f"{sum_unmarked} * {int(nr)} = {int(nr) * sum_unmarked}")
                quit()
    print(-1)
