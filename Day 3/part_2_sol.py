PUZZLE_INPUT_FILE = "puzzle_input.txt"


if __name__ == "__main__":
    puzzle_input = open(PUZZLE_INPUT_FILE, "r").readlines()
    puzzle_input = [number.strip() for number in puzzle_input]

    remaining_numbers_oxygen = puzzle_input
    remaining_numbers_c02 = puzzle_input

    for i in range(len(puzzle_input[0])):
        numbers_i_oxygen = [[], []]
        numbers_i_c02 = [[], []]
        if len(remaining_numbers_oxygen) > 1:
            for number in remaining_numbers_oxygen:
                numbers_i_oxygen[int(number[i])].append(number)
            if len(numbers_i_oxygen[0]) > len(numbers_i_oxygen[1]):
                remaining_numbers_oxygen = numbers_i_oxygen[0]
            else:
                remaining_numbers_oxygen = numbers_i_oxygen[1]
        if len(remaining_numbers_c02) > 1:
            for number in remaining_numbers_c02:
                numbers_i_c02[int(number[i])].append(number)
            if len(numbers_i_c02[0]) > len(numbers_i_c02[1]):
                remaining_numbers_c02 = numbers_i_c02[1]
            else:
                remaining_numbers_c02 = numbers_i_c02[0]

    gamma_rate_bin = remaining_numbers_oxygen[0]
    epsilon_rate_bin = remaining_numbers_c02[0]
    print(gamma_rate_bin)
    print(epsilon_rate_bin)
    gamma_rate = int(gamma_rate_bin, 2)
    epsilon_rate = int(epsilon_rate_bin, 2)

    print(f"{gamma_rate} * {epsilon_rate} = {gamma_rate*epsilon_rate}")
