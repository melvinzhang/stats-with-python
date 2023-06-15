import random

def play(switch):
    doors = [1, 2, 3]
    pair = (random.choice(doors), random.choice(doors))
    winning_door, chosen_door = pair
    opened_door = random.choice([d for d in doors if d not in pair])
    if switch:
        chosen_door = sum(doors) - chosen_door - opened_door
    return winning_door == chosen_door

rounds = 1000
wins = {True: 0.0, False: 0.0}
for _ in range(rounds):
    for switch in (True, False):
        wins[switch] += 1/rounds if play(switch) else 0.0

print(wins)
