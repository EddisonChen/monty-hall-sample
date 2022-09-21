import random

wins = []
losses = []
stay_wins = []
stay_losses = []

def run_trial(win_door, selected_door):
    if selected_door == win_door:
        wins.append(1)
    elif selected_door != win_door:
        losses.append(1)

def print_results():
    win_percentage = sum(list(wins))/(sum(list(wins)) + sum(list(losses)))
    print(f"Always switching, your win percentage is {win_percentage * 100}%")

def print_stay_results():
    win_percentage = sum(list(stay_wins))/(sum(list(stay_wins)) + sum(list(stay_losses)))
    print(f"Never switching, your win percentage is {win_percentage * 100}%")

def switch_doors():
    i = 0
    while i < 1000000:
        selected_door = random.choice([1, 2, 3])
        win_door = random.choice([1, 2, 3])
        if win_door == selected_door:
            if win_door == 1 and selected_door == 1:
                selected_door = random.choice([2, 3])
            elif win_door == 2 and selected_door == 2:
                selected_door = random.choice([1, 3])
            elif win_door == 3 and selected_door == 3:
                selected_door = random.choice([1, 2])
        elif win_door != selected_door:
            if win_door == 1 and selected_door == 2:
                selected_door = 1
            elif win_door == 1 and selected_door == 3:
                selected_door = 1
            elif win_door == 2 and selected_door == 3:
                selected_door = 2
            elif win_door == 2 and selected_door == 1:
                selected_door = 2
            elif win_door == 3 and selected_door == 1:
                selected_door = 3
            elif win_door == 3 and selected_door == 2:
                selected_door = 3
        run_trial(win_door, selected_door)
        i += 1
    print_results()

def stay_door():
    i = 0
    while i < 1000000:
        selected_door = random.choice([1, 2, 3])
        win_door = random.choice([1, 2, 3])
        if win_door == selected_door:
            stay_wins.append(1)
        elif win_door != selected_door:
            stay_losses.append(1)
        run_trial(win_door, selected_door)
        i += 1
    print_stay_results()

def both_sims():
    switch_doors()
    stay_door()

both_sims()