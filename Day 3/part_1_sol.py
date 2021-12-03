PUZZLE_INPUT_FILE = "puzzle_input.txt"


def argmax(lst):
    max_lst = max(lst)
    for i in range(len(lst)):
        if lst[i] == max_lst:
            return i
    raise Exception()


def argmin(lst):
    min_lst = min(lst)
    for i in range(len(lst)):
        if lst[i] == min_lst:
            return i
    raise Exception()


if __name__ == "__main__":
    puzzle_input = open(PUZZLE_INPUT_FILE, "r").readlines()
    binary_counter = [[0, 0] for _ in puzzle_input[0].strip()]

    for number in puzzle_input:
        for i, bit in enumerate(number.strip()):
            binary_counter[i][int(bit)] += 1

    gamma_rate_bin = "".join([str(argmax(pair)) for pair in binary_counter])
    epsilon_rate_bin = "".join([str(argmin(pair)) for pair in binary_counter])
    print(gamma_rate_bin)
    print(epsilon_rate_bin)
    gamma_rate = int(gamma_rate_bin, 2)
    epsilon_rate = int(epsilon_rate_bin, 2)

    print(f"{gamma_rate} * {epsilon_rate} = {gamma_rate*epsilon_rate}")
