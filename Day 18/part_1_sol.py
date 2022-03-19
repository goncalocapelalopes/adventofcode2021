PUZZLE_INPUT_FILE = "puzzle_input.txt"
import re
from math import floor, ceil

def magnitude(lst):
    while re.match("^[0-9]+$", lst) is None:
        lst = re.sub("\[([0-9]+),([0-9]+)\]", lambda x: f"{3*int(x.group(1))+2*int(x.group(2))}", lst)
    return int(lst)

def str2pair(pair_str):
    return list((int(pair_str.split(",")[0][1:]),
                int(pair_str.split(",")[1][0:-1])))

def get_nmbr_at_depth(lst, depth_goal=4):
    depth = 0
    start = 0
    end = 0
    gotcha = False
    for i, char in enumerate(lst):
        if depth == depth_goal and char == "[":
            gotcha = True
            start = i
        elif depth == depth_goal and char == "]" and gotcha:
            return start, i+1
        else:
            if char == "[":
                depth += 1
            elif char == "]":
                depth -= 1
    return None, None
        

def explode(lst):
    start, end = get_nmbr_at_depth(lst)
    if start is None:
        return lst
    explodee = str2pair(lst[start:end])

    left = re.sub("(\d+)(?!.*\d)", lambda x: f"{explodee[0] + int(x.group(0))}",lst[:start], 1)
    right = re.sub("([0-9]+)", lambda x: f"{explodee[1] + int(x.group(0))}", lst[end:], 1)

    return left + "0" + right

def split(lst):
    return re.sub("([0-9]{2})", lambda x: f"[{floor(int(x.group(0))/2)},{ceil(int(x.group(0))/2)}]", lst, 1)

def reduce(lst):
    while True:
        new_lst = explode(lst)
        if new_lst != lst:
            lst = new_lst
            continue
        else:
            new_lst = split(lst)
            if new_lst == lst:
                break
            else:
                lst = new_lst
                continue
    return lst
    

if __name__ == "__main__":
    lines = open(PUZZLE_INPUT_FILE, "r").readlines()
    puzzle = lines[0].rstrip("\n")
    for line in lines[1:]:
        puzzle = reduce("["+puzzle+","+line.rstrip("\n")+"]")


    print(magnitude(puzzle))
    print(puzzle)

