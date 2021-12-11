from collections import deque

PUZZLE_INPUT_FILE = "puzzle_input.txt"

scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

pairs = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

closing_chars = ")]}>"
if __name__ == "__main__":
    lines = open(PUZZLE_INPUT_FILE, "r").read().splitlines()
    expected_stack = deque()
    sum_scores = 0
    for line in lines:
        for char in line:
            if char in closing_chars:
                expected_char = expected_stack.popleft()
                if char != expected_char:
                    print(f"Expected {expected_char}, but found {char} instead.")
                    sum_scores += scores[char]
            else:
                expected_stack.appendleft(pairs[char])
    print(sum_scores)