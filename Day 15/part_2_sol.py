from math import sqrt
PUZZLE_INPUT_FILE = "puzzle_input.txt"


class State:
    def __init__(self, row, col, distance, h, parent):
        self._row = row
        self._col = col
        if parent is not None:
            self._g = parent._g + distance
        else:
            self._g = distance
        self._h = h
        self._parent = parent

    def f(self):
        return self._g + self._h

    def __repr__(self):
        return f"({self._row}, {self._col}, g={self._g}, f={self.f()})"


def euclidian_dist(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1]-p2[1])**2)


def a_star(start, space):
    open_nodes = [start]
    closed_nodes = [[State(row, col, space[row][col], float("inf"), None) for
                     col in range(len(space[row]))] for row in range(len(space))]
    open_fast = [[State(row, col, space[row][col], float("inf"), None) for
                     col in range(len(space[row]))] for row in range(len(space))]
    while len(open_nodes) > 0:
        q, open_nodes = open_nodes[0], open_nodes[1:]
        open_fast[q._row][q._col] = State(q._row, q._col, space[q._row][q._col], float("inf"), None)

        open_nodes, open_fast = generate_successors(q, space, open_nodes, closed_nodes, open_fast)
        if type(open_nodes) != list:
            return open_nodes

        if q.f() < closed_nodes[q._row][q._col].f():
            closed_nodes[q._row][q._col] = q
    return -1


def generate_successors(state, space, open_nodes, closed_nodes, open_fast):
    around = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    limit_row = len(space[0])
    limit_col = len(space)

    for ar in around:

        row = state._row + ar[0]
        col = state._col + ar[1]
        if row < 0 or row >= limit_row or \
           col < 0 or col >= limit_col:
            continue
        else:
            succ = State(row, col, space[row][col], euclidian_dist((row, col), (limit_row, limit_col)), state)
            if isGoal(succ, space):
                return succ, None
            else:

                skip_succ = False
                if closed_nodes[succ._row][succ._col].f() <= succ.f() or\
                   open_fast[succ._row][succ._col].f() <= succ.f():
                    skip_succ = True

                if not skip_succ:
                    highest = True
                    for i in range(len(open_nodes)):
                        if open_nodes[i].f() > succ.f():
                            if len(open_nodes) > 1:
                                open_nodes = open_nodes[:i] + [succ] + open_nodes[i:]
                            else:
                                open_nodes = [succ] + open_nodes
                            highest = False
                            break
                    if highest:
                        open_nodes = open_nodes + [succ]
                    open_fast[row][col] = succ

    return open_nodes, open_fast


def new_val(val, add):
    if val + add >= 10:
        return val + add - 9
    else:
        return val + add


def isGoal(state, space):
    limit_row = len(space[0])
    limit_col = len(space)

    return (state._row, state._col) == (limit_row-1, limit_col-1)


def build_cave(lines):
    new_lines = []
    for new_row_i in range(5):

        for row_i in range(len(lines)):
            new_row = []
            for new_col_i in range(5):
                for col_i in range(len(lines[0])):
                    new_row.append(new_val(lines[row_i][col_i], new_row_i+new_col_i))
            new_lines.append(new_row)
    return new_lines


if __name__ == "__main__":
    lines = open(PUZZLE_INPUT_FILE, "r").read().splitlines()
    space = [list(map(int, list(line))) for line in lines]
    space = build_cave(space)
    start = State(0, 0, 0, 0, None)

    goal = a_star(start, space)

    if goal == -1:
        print(-1)
    else:
        print(goal._g)
