PUZZLE_INPUT_FILE = "puzzle_input.txt"


class Cave:

    def __init__(self, name):
        self.name = name
        self.paths = []

    def isBig(self):
        return self.name.isupper()

    def isSmall(self):
        return self.name.islower() and not self.isEnd() and not self.isStart()

    def addPath(self, cave):
        self.paths.append(cave)

    def isStart(self):
        return self.name == "start"

    def isEnd(self):
        return self.name == "end"

    def __repr__(self):
        return self.name


class State:

    def __init__(self, cave, visited, visit_twice_name=None, visit_twice_count=0):
        self.cave = cave
        self.visited = visited
        self.visit_twice_name = visit_twice_name
        self.visit_twice_count = visit_twice_count

    def __repr__(self):
        return self.cave.name + "(2-" + str(self.visit_twice_name) + ")"

    def next_states(self):
        possibles = []
        for c in self.cave.paths:
            if (c.isSmall() and
                c.name in self.visited and
                self.visit_twice_name == c.name and
                self.visit_twice_count == 2):
                continue
            elif (c.isSmall() and
                  c.name in self.visited and
                  self.visit_twice_name is not None and
                  self.visit_twice_name != c.name):
                continue
            elif (c.isSmall() and
                  c.name in self.visited and
                  self.visit_twice_name is None):
                continue
            elif (c.isSmall() and
                  c.name in self.visited and
                  self.visit_twice_name == c.name and
                  self.visit_twice_count < 2):
                possibles.append(State(c, self.visited + [c.name], c.name, self.visit_twice_count+1))
            elif (c.isSmall() and
                  c.name not in self.visited and
                  self.visit_twice_name is None):
                possibles.append(State(c, self.visited + [c.name], c.name, 1))
                possibles.append(State(c, self.visited + [c.name]))
            elif c.name == "start":
                continue
            else:
                possibles.append(State(c, self.visited + [c.name], self.visit_twice_name, self.visit_twice_count))

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
                if state.visited not in all_paths:
                    all_paths.append(state.visited)
            else:
                new_states.extend(state.next_states())
        states = new_states
        if len(new_states) == 0:
            break
    print(len(all_paths))
