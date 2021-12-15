from collections import Counter
from math import ceil
PUZZLE_INPUT_FILE = "puzzle_input.txt"
STEPS = 40


def get_resulting_pairs(pair, rules):
    return pair[0] + rules[pair], rules[pair] + pair[1]


def calc_answer(pair_counter):
    counter_dict = {}
    for pair in pair_counter.keys():
        if pair[0] not in counter_dict:
            counter_dict[pair[0]] = 0
        if pair[1] not in counter_dict:
            counter_dict[pair[1]] = 0
        counter_dict[pair[0]] += pair_counter[pair]
        counter_dict[pair[1]] += pair_counter[pair]
    counter = Counter(counter_dict)
    return counter.most_common()[0][1] - counter.most_common()[-1][1]


if __name__ == "__main__":
    lines = open(PUZZLE_INPUT_FILE, "r").read().splitlines()

    template = lines[0]
    rules = {line.split(" -> ")[0]:line.split(" -> ")[1] for line in lines[2:]}
    pair_counter = {key:0 for key in rules.keys()}

    for i in range(len(template)-1):
        pair_counter[template[i:i+2]] += 1

    for step in range(STEPS):
        new_pair_counter = pair_counter.copy()
        for key in pair_counter.keys():
            if pair_counter[key] == 0:
                continue
            new_pairs = get_resulting_pairs(key, rules)
            new_pair_counter[key] -= pair_counter[key]
            new_pair_counter[new_pairs[0]] += pair_counter[key]
            new_pair_counter[new_pairs[1]] += pair_counter[key]
        pair_counter = new_pair_counter
    print(ceil(calc_answer(pair_counter)/2))
