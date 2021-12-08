PUZZLE_INPUT_FILE = "puzzle_input.txt"


if __name__ == "__main__":
    entries = open(PUZZLE_INPUT_FILE, "r").readlines()
    digit_outputs = [entry.split("|")[1].strip().split() for entry in entries]

    sum1478 = 0
    for d_o in digit_outputs:
        for value in d_o:
            if len(value) in (2, 4, 3, 7):
                sum1478 += 1

    print(sum1478)
