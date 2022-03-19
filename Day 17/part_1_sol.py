import re
PUZZLE_INPUT_FILE = "puzzle_input.txt"



if __name__ == "__main__":
    line = open(PUZZLE_INPUT_FILE, "r").read()
    m = re.match("target area: x=(-?[0-9]+)..(-?[0-9]+), y=-(-?[0-9]+)..(-?[0-9]+)", line)
    x_min, x_max, y_min, y_max = [int(m.group(i)) for i in range(1, 5)] 
    success = False
    x, y = (0, 0)

    y_vel0 = abs(y_min) - 1
    print(int((y_vel0 * (y_vel0+1))/2))


            