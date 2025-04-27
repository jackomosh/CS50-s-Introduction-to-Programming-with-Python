# from random import choice

# coin = choice(["heads", "tails"])

# print(coin)

import random

# number = random.randint(1, 6)
# print(number)

names = ["Jack", "James", "Raul", "Olivia"]
random.shuffle(names)

for name in names:
    print(name)