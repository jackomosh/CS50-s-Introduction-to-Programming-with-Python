import random

cards = ["jack", "queen", "king"]

# print(random.sample(cards, k=2))

print(random.choices(cards, weights=[75, 20, 5], k = 2))