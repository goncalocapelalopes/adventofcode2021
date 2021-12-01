PUZZLE_INPUT_FILE = "puzzle_input.txt"
WINDOW_SIZE = 3

if __name__ == "__main__":
    puzzle_input = open(PUZZLE_INPUT_FILE, "r").readlines()
    puzzle_input = [int(i) for i in puzzle_input]

    sum_array = []
    for i in range(WINDOW_SIZE, len(puzzle_input)+1):
        sum_array.append(sum(puzzle_input[i-(WINDOW_SIZE):i]))

    times = 0
    for i in range(1, len(sum_array)):
        if sum_array[i] > sum_array[i-1]:
            times += 1
    print(times)
