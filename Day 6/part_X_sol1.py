PUZZLE_INPUT_FILE = "puzzle_input.txt"
DAYS = 256
BABY_FIRST_TIMER = 9
FISH_TIMER = 7

def calc_n_children(remaining_days, baby, initial_counter=-1):
    children = []
    if baby:
        n_children = (remaining_days >= BABY_FIRST_TIMER) * 1
        n_children += (max(remaining_days - BABY_FIRST_TIMER, 0) // FISH_TIMER)
        children.extend([remaining_days-BABY_FIRST_TIMER-(FISH_TIMER*i) for i in range(n_children)])
    else:
        n_children = max(remaining_days + (FISH_TIMER-1 - initial_counter), 0) // FISH_TIMER
        children.extend([remaining_days - (initial_counter+1) - (FISH_TIMER*i) for i in range(n_children)])
    if len(children) == 0:
        return 0
    else:
        return len(children) + sum([calc_n_children(remaining_days, True) for remaining_days in children if remaining_days >= 0])


if __name__ == "__main__":
    fish = open(PUZZLE_INPUT_FILE, "r").readline().split(",")
    fish = [int(f) for f in fish]
    sum_fish = sum([calc_n_children(DAYS, False, initial_counter=init_count) for init_count in fish]) + len(fish)

    print(sum_fish)
