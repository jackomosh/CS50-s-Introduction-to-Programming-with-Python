# A I P C R H G

Words = {
    "Pair": 4,
    "Hair": 4,
    "Chair": 5,
    "Grip": 4,
    "Crip": 4,
    "Chip": 4,
    "Carp": 4,
    "Rich": 4,
    "Graph": 5,
    "Parch": 5,
}

def main():
    proceed = input("To play the spelling bee game, (type Y / y) ")
    # points = 0
    if proceed == "Y" or proceed == "y":
        while True:
            print(f"{len(Words)} words left!")
            answer = input("Make a 4 / 5 letter word with this letters: (A, I, P, C, R, H, G) ")
            # if answer == "Graphic":
            #     Words.clear()
            #     print("You are a champ")
            #     return
            if answer in Words.keys():
                points = Words.pop(answer)
                # total = Words.pop(answer) + points
                # print("You have earned one point")
                print(f"You have earned", points, "points")
                # print("Your Total Points are", total)
                # del Words[answer]
                if not Words:
                    print("Hurrrraaaaayyy!! You found all words")
                    # print(f"You have", points, "points in total")
                    return
                continue
            else:
                print("Try again")
    else:
        print("Not eligible")

    # print out the results later after the game has ended
    """"
    for word, points in Words.item:
        print(f"{word} was worth {points}")
    """
main()



