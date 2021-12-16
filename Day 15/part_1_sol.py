PUZZLE_INPUT_FILE = "puzzle_input.txt"


class State:
    def __init__(self, row, col, distance):
        self._row = row
        self._col = col
        self._orig_distance = distance
        self._distance = float("inf")

    def update_distance(self, new_distance):
        if new_distance + self._orig_distance < self._distance:
            self._distance = new_distance + self._orig_distance

    def __repr__(self):
        return f"({self._row}, {self._col}, distance={self._distance})"


def dijkstra(start, space):
    visited = [start]
    unvisited = space.copy()
    unvisited[0][0] = None

    curr_state = start
    while not isGoal(curr_state, space):
        unvisited = updateNeighbours(curr_state, visited, unvisited, space)
        flat = [state for row in unvisited for state in row if state is not None]
        curr_state = sorted(flat, key=lambda x: x._distance)[0]
        unvisited[curr_state._row][curr_state._col] = None
        visited.append(curr_state)  # only need to add coords to visited
    return curr_state


def updateNeighbours(state, visited, unvisited, space):
    limit_row = len(space[0])
    limit_col = len(space)
    around = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    res = []
    for ar in around:
        row = state._row + ar[0]
        col = state._col + ar[1]
        if row < 0 or row >= limit_row or col < 0 or col >= limit_col or (row, col) in [(vis._row, vis._col) for vis in visited]:
            continue
        else:
            unvisited[row][col].update_distance(state._distance)
            res.append(unvisited[row][col])
    return unvisited


def isGoal(state, space):
    limit_row = len(space[0])
    limit_col = len(space)

    return (state._row, state._col) == (limit_row-1, limit_col-1)






if __name__ == "__main__":
    lines = open(PUZZLE_INPUT_FILE, "r").read().splitlines()
    lines = [list(map(int, list(line))) for line in lines]
    space = [[State(row, col, lines[row][col]) for col in range(len(lines[row]))] for row in range(len(lines))]
    start = space[0][0]
    start.update_distance(0)
    goal = dijkstra(start, space)
    print(goal._distance-start._distance)
