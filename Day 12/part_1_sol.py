PUZZLE_INPUT_FILE = "puzzle_input.txt"


class Cave:

    def __init__(self, name):
        self.name = name
        self.paths = []

    def isBig(self):
        return self.name.isupper()

    def isSmall(self):
        return self.name.islower()

    def addPath(self, cave):
        self.paths.append(cave)

    def isStart(self):
        return self.name == "start"

    def isEnd(self):
        return self.name == "end"

    def __repr__(self):
        return self.name


class State:

    def __init__(self, cave, visited):
        self.cave = cave
        self.visited = visited

    def next_possibles(self):
        possibles = []
        for c in self.cave.paths:
            if not (c.isSmall() and c in self.visited):
                possibles.append(c)
        return possibles

if __name__ == "__main__":
    lines = open(PUZZLE_INPUT_FILE, "r").read().splitlines()
    caves = {}
    all_paths = []
    for line in lines:
        left, right = line.split("-")
        if left in caves.keys():
            left = caves[left]
        else:
            caves[left] = Cave(left)
            left = caves[left]
        if right in caves.keys():
            right = caves[right]
        else:
            caves[right] = Cave(right)
            right = caves[right]
        caves[left.name].addPath(right)
        caves[right.name].addPath(left)

    states = [State(caves["start"], [caves["start"]])]
    while True:
        new_states = []
        for state in states:
            if state.cave.isEnd():
                all_paths.append(state.visited)
            else:
                possibles = state.next_possibles()
                new_states.extend([State(cave, state.visited + [cave]) for cave in possibles])
        states = new_states
        if len(new_states) == 0:
            break
    print(len(all_paths))