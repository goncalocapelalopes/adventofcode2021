PUZZLE_INPUT_FILE = "puzzle_input.txt"
DAYS = 256
BABY_FIRST_TIMER = 9
FISH_TIMER = 7



def get_children(initial_counter, remaining_days, baby):
    if remaining_days >= DAYS:
        return []

    if baby:
        children = (remaining_days +9 <= DAYS) * [remaining_days + 9]
        children.extend([i for i in range(remaining_days+9-(FISH_TIMER-1-6), DAYS+1, FISH_TIMER)][1:])
    else:
        children = [i for i in range(-(FISH_TIMER-1-initial_counter), DAYS+1, FISH_TIMER)][1:]
    return children

if __name__ == "__main__":
    fish_0 = open(PUZZLE_INPUT_FILE, "r").readline().split(",")
    fish_0 = [int(f) for f in fish_0]
    sum_fish = len(fish_0)

    days_fish = {}
    for f in fish_0:
        children = get_children(f, 0, False)
        for c in children:
            if str(c) not in days_fish.keys():
                days_fish[str(c)] = 1
            else:
                days_fish[str(c)] += 1
    while len(days_fish.keys()) > 0:

        key = list(days_fish.keys())[0]
        n_fish = days_fish[key]

        children = get_children(8, int(key), True)

        for c in children:
            if str(c) not in days_fish.keys():
                days_fish[str(c)] = 1 * n_fish
            else:
                days_fish[str(c)] += 1 * n_fish
        sum_fish += n_fish
        days_fish.pop(key)

    print(sum_fish)
