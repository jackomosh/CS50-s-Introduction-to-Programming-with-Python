def main():
    history = []

    while True:
        moves = input("Move either: Left, Right, Up / Down? ")

        if moves == "Undo":
            deleted = history.pop()
            print(history)
            print("Deleted: ", deleted)
        elif moves == "Restart":
            history.clear()
            print(history)
        else:
            history.append(moves)
            print(history)

main()