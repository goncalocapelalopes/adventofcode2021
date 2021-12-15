from collections import Counter

PUZZLE_INPUT_FILE = "puzzle_input.txt"
STEPS = 40


def calc_answer(polymer):
    counter = Counter(polymer)
    return counter.most_common()[0][1] - counter.most_common()[-1][1]


if __name__ == "__main__":
    lines = open(PUZZLE_INPUT_FILE, "r").read().splitlines()

    polymer = lines[0]
    rules = {line.split(" -> ")[0]:line.split(" -> ")[1] for line in lines[2:]}

    for step in range(STEPS):
        new_polymer = ""
        for i in range(len(polymer)-1):
            new_polymer += polymer[i] + rules[polymer[i:i+2]]
        new_polymer += polymer[-1]
        polymer = new_polymer
    print(calc_answer(polymer))
