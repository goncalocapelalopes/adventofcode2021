PUZZLE_INPUT_FILE = "puzzle_input.txt"


def print_paper(paper):
    for line in paper:
        print("".join(line))


def fold_x(paper, x):
    paper0 = [row[:x] for row in paper]
    paper1 = [row[x+1:] for row in paper]
    last_col = len(paper0[0])-1

    for i in range(len(paper0)):
        for j in range(len(paper0[0])):
            if paper1[i][last_col-j] == "#":
                paper0[i][j] = "#"

    return paper0


def fold_y(paper, y):
    paper0 = paper[:y]
    paper1 = paper[y+1:]
    last_row = len(paper0)-1

    for i in range(len(paper0)):
        for j in range(len(paper0[0])):
            if paper1[last_row-i][j] == "#":
                paper0[i][j] = "#"

    return paper0


def countcardinals(paper):
    return sum([len([point for point in row if point == "#"]) for row in paper])


if __name__ == "__main__":
    lines = open(PUZZLE_INPUT_FILE, "r").read().splitlines()
    paper = []
    dot_x_coords = []
    dot_y_coords = []

    # BUILD PAPER
    for i in range(len(lines)):
        if lines[i] == "":
            break
        x, y = map(int, lines[i].split(","))
        dot_x_coords.append(x)
        dot_y_coords.append(y)

    n_rows = 0
    n_cols = 0
    for i in range(len(dot_x_coords)+1, len(lines)):
        orientation, line = lines[i].split("=")[0][-1], int(lines[i].split("=")[1])
        if orientation == "x" and n_cols == 0:
            n_cols = line * 2 + 1
        elif orientation == "y" and n_rows == 0:
            n_rows = line * 2 + 1

    paper.extend([["." for _ in range(n_cols+1)] for _ in range(n_rows+1)])
    for x, y in zip(dot_x_coords, dot_y_coords):
        paper[y][x] = "#"

    # INSTRUCTIONS
    for i in range(len(dot_x_coords)+1, len(lines)):
        orientation, line = lines[i].split("=")[0][-1], int(lines[i].split("=")[1])
        if orientation == "x":
            paper = fold_x(paper, line)
        else:
            paper = fold_y(paper, line)
        break

    print_paper(paper)
    print(countcardinals(paper))
