from math import ceil, sqrt
import re
PUZZLE_INPUT_FILE = "puzzle_input.txt"

def update_xvel(xvel):
    if xvel > 0:
        xvel -= 1
    elif xvel < 0:
        xvel += 1
    return xvel

def update_yvel(yvel):
    return yvel-1

if __name__ == "__main__":
    line = open(PUZZLE_INPUT_FILE, "r").read()
    m = re.match("target area: x=(-?[0-9]+)..(-?[0-9]+), y=(-?[0-9]+)..(-?[0-9]+)", line)
    x_min, x_max, y_min, y_max = [int(m.group(i)) for i in range(1, 5)] 
    success = False

    min_xvel = round((-1 + sqrt(1 + 4 * 2 * x_min)) / 2)
    max_xvel = x_max

    min_yvel = y_min
    max_yvel = abs(y_min) - 1
    
    valids = []

    for xvel in range(min_xvel, max_xvel+1):
        for yvel in range(min_yvel, max_yvel+1):
            y = 0
            
            # fastforward to yvel and xvel at y=0
            if yvel <= 0:
                x = 0
                xvel_curr = xvel
            elif xvel <= (2*yvel + 1):
                x = (xvel*(xvel+1))/2  
                xvel_curr = 0
            else:
                x = (xvel*(xvel+1))/2 - ((xvel - (2*yvel+1))*((xvel - (2*yvel+1)) + 1))/2 
                xvel_curr = xvel - (2*yvel+1)
                

            if yvel == 0:
                yvel_curr = 0
            else:
                yvel_curr = (-(yvel+1)) if (yvel > 0) else (yvel)

            while True:
                if x > x_max or y < y_min:
                    break
                if x >= x_min and x <= x_max and y >= y_min and y <= y_max:
                    valids.append((xvel, yvel))

                    break
                else:
                    x += xvel_curr
                    y += yvel_curr
                    xvel_curr = update_xvel(xvel_curr)
                    yvel_curr = update_yvel(yvel_curr)

    print(len(valids))


            