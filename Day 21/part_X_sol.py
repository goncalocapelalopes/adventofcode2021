import re

PUZZLE_INPUT_FILE = "puzzle_input.txt"
TARGET_SCORE = 21

def update_die(die_side):
    if die_side == 100:
        return 1
    else:
        return die_side + 1

def update_position(position, offset):
    new_position = (position + offset) % 10
    if new_position == 0:
        return 10
    return new_position

def make_move(player, points, position, die_side):
    offset = 0
    dice = []
    for i in range(3):
        dice.append(die_side)
        die_side = update_die(die_side)

    offset = sum(dice)
    position = update_position(position, offset)
    print(f"Player {player} rolls {dice} and moves to space {position} for a total score of {points+position}.")
    return position, die_side


if __name__ == "__main__":
    lines = open(PUZZLE_INPUT_FILE, "r").readlines()
    positions = {}
    points = {}
    for line in lines:
        match = re.findall("\d", line.strip("\n"))
        positions[match[0]] = int(match[1])
        points[match[0]] = 0
    
    rolls = 0
    die_side = 1
    get_out = False
    winner = None

    while not get_out:
        for player in positions.keys():
            positions[player], die_side = make_move(player, points[player], positions[player], die_side)
            points[player] += positions[player]
            rolls += 3
            #input()
            if points[player] >= TARGET_SCORE:
                winner = player
                print("Player", str(player), "wins with", str(points[player]), "points after", str(rolls), "dice rolls!")
                get_out = True
                #print(str(points[player]), "*", str(rolls), "=", str(points[player]*rolls))
                break

    for player in positions.keys():
        if player != winner:
            print("Player", str(player), "loses with", str(points[player]), "points after", str(rolls), "dice rolls!")
            print(str(points[player]), "*", str(rolls), "=", str(points[player]*rolls))