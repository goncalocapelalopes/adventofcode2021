PUZZLE_INPUT_FILE = "puzzle_input.txt"


def str_intersect(str1, str2):
    return len(set(str1).intersection(str2))

def get_pattern_map(patterns):
    digit_map = {}
    patts235 = []
    patts069 = []
    for patt in patterns:
        if len(patt) == 2:
            digit_map["1"] = "".join(sorted(patt))
        elif len(patt) == 4:
            digit_map["4"] = "".join(sorted(patt))
        elif len(patt) == 3:
            digit_map["7"] = "".join(sorted(patt))
        elif len(patt) == 7:
            digit_map["8"] = "".join(sorted(patt))
        elif len(patt) == 5:
            patts235.append("".join(sorted(patt)))
        else:
            patts069.append("".join(sorted(patt)))

    for patt in patts235:
        if str_intersect(patt, digit_map["1"]) == 2:
            digit_map["3"] = patt
        elif str_intersect(patt, digit_map["4"]) == 3:
            digit_map["5"] = patt
        else:
            digit_map["2"] = patt

    for patt in patts069:
        if str_intersect(patt, digit_map["1"]) == 1:
            digit_map["6"] = patt
        elif str_intersect(patt, digit_map["4"]) == 4:
            digit_map["9"] = patt
        else:
            digit_map["0"] = patt

    return {v: k for k, v in digit_map.items()}


if __name__ == "__main__":
    entries = open(PUZZLE_INPUT_FILE, "r").readlines()
    entries = [entry.split("|") for entry in entries]

    sum_outputs = 0
    for entry in entries:
        pattern_map = get_pattern_map(entry[0].split())
        output = "".join([pattern_map["".join(sorted(pattern))] for pattern in entry[1].split()])
        sum_outputs += int(output)
    print(sum_outputs)
