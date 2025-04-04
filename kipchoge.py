def main():
    pace = get_pace(Kilometers = 26.7, Minutes = 0)
    print(f"You will need to run each kilometer in {pace} minutes")

def get_pace(Kilometers, Minutes):
    if not Minutes > 0:
        raise ValueError("Minutes is invalid")

    return Minutes / Kilometers

main()