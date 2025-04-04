def main():
    message = input(">")
    message = convert(message)
    print(message)

def convert(str):

    # words = {
    #     ":)": "🙂",
    #     ":(": "🙁"
    # }

    str = str.replace(":)", "🙂")
    str = str.replace(":(", "🙁")

    return str

    

main()