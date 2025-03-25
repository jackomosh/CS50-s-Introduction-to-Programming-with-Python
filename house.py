house_name = input("Which House Tree are you from? ")

match house_name:
    case "Jack" | "Angelina":
        print("Okoth's Family")
    case "Cate" | "Maurice":
        print("Ogonda's Family")
    case "Milly" | "Ken":
        print("Kaunda's Family")
    case "Caro" | "Paul":
        print("Wagandi's Family")
    case _:
        print("Who?")