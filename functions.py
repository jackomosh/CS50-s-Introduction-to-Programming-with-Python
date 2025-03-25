def greet(us):
    print("Hello", us)
    


def main():
    name = input("What is your name? ")
    name = name.capitalize()
    greet(name)


main()
