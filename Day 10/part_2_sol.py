from collections import deque
from math import ceil, floor

PUZZLE_INPUT_FILE = "puzzle_input.txt"

scores_char = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

pairs = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}


def calc_line_score(closing):
    score = 0
    for char in closing:
        score *= 5
        score += scores_char[char]
    return score


closing_chars = ")]}>"

if __name__ == "__main__":
    lines = open(PUZZLE_INPUT_FILE, "r").read().splitlines()
    expected_stack = deque()

    scores = []
    for line in lines:
        for char in line:
            if char in closing_chars:
                expected_char = expected_stack.popleft()
                if char != expected_char:
                    print(f"Expected {expected_char}, but found {char} instead.")
                    expected_stack = deque()
                    break
            else:
                expected_stack.appendleft(pairs[char])
        if len(expected_stack) > 0:
            scores.append(calc_line_score(expected_stack))
            expected_stack = deque()
    scores = sorted(scores)
    print(scores[floor(len(scores)/2)])
