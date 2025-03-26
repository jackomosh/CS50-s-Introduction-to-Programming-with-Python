distances = {
    "Voyager 1": 163,
    "Voyager 2": 132,
    "Pioneer 10": 145,
    "New Horizons": 58,
    "Pioneer 11": 40
}

def main():
    for name in distances.keys():
        print(f"{name} is {distances[name]}")


main()

