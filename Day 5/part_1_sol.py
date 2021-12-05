PUZZLE_INPUT_FILE = "puzzle_input.txt"


def is_diagonal(vent_line):
    start, finish = vent_line["start"], vent_line["finish"]
    return start[0] != finish[0] and start[1] != finish[1]


def sign(boolean):
    if boolean:
        return 1
    else:
        return -1


def get_line_points(start, finish):
    points = [start]
    x = start[0]
    y = start[1]

    if start[0] == finish[0]:
        x_sign = 0
    else:
        x_sign = sign(start[0] < finish[0])
    if start[1] == finish[1]:
        y_sign = 0
    else:
        y_sign = sign(start[1] < finish[1])
    while x != finish[0] or y != finish[1]:
        x += x_sign
        y += y_sign
        points.append((x, y))
    return points


if __name__ == "__main__":
    vent_lines = []
    puzzle_input = open(PUZZLE_INPUT_FILE, "r").readlines()

    # build vent line data structure
    max_x = 0
    max_y = 0
    for line in puzzle_input:
        start, finish = line.split(" -> ")
        start = tuple(map(int, start.split(",")))
        finish = tuple(map(int, finish.split(",")))
        max_x = max(max_x, start[0], finish[0])
        max_y = max(max_y, start[1], finish[1])
        vent_line = {"start": start, "finish": finish}
        if not is_diagonal(vent_line):
            vent_lines.append(vent_line)
    diagram = [[0] * (max_x+1) for _ in range(max_y+1)]

    overlaps = 0
    for line in vent_lines:
        points = get_line_points(line["start"], line["finish"])
        for point in points:
            diagram[point[1]][point[0]] += 1
            overlaps += (diagram[point[1]][point[0]] == 2) * 1

    print(overlaps)
