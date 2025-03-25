def main():
    difficulty = input("Difficult or Casual? ")

    # boolean expression to check for true / false before we go ahead and execute the program
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter A Valid Difficulty Level")
        return

    players = input("Multiplayer or Single-Player? ")

    if not (players == "Multiplayer" or players == "Single-Player"):
        print("Enter A Valid Player Option")
        return

    if difficulty == "Difficult" and players == "Multiplayer":
            recommendations("Poker")
    elif difficulty == "Difficult" and players == "Single-Player":
            recommendations("Klondike")
    elif difficulty == "Casual" and players == "Multiplayer":
            recommendations("Hearts")
    else:
            recommendations("Clock")

def recommendations(game):
    print("We Recommend", game)

main()