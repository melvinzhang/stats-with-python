from random import choice
from statistics import mean

days = range(365)

def same_birthday_size():
    bdays = set()
    while (chosen := choice(days)) not in bdays:
        bdays.add(chosen)
    return len(bdays) + 1

sizes = [same_birthday_size() for _ in range(1000)]

print(mean(sizes))
