names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.strip())

for name in sorted(names):
    print("Hello", name)